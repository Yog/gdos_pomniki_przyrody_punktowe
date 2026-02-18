from org.openstreetmap.josm.gui import MainApplication
from org.openstreetmap.josm.data.osm import Node, TagMap
from org.openstreetmap.josm.data import UndoRedoHandler
from org.openstreetmap.josm.command import ChangeCommand, DeleteCommand, SequenceCommand

# 1. Get the current edit layer (works for GeoJSON layers)
layer = MainApplication.getLayerManager().getEditLayer()

if layer and layer.data:
    # Use selection if available, otherwise process all nodes
    selected_nodes = layer.data.getSelectedNodes()
    if not selected_nodes:
        selected_nodes = layer.data.getNodes()

    groups = {}
    for node in selected_nodes:
        # Group by coordinates (7 decimal places matches GeoJSON precision)
        key = "{:.7f},{:.7f}".format(node.getCoor().lat(), node.getCoor().lon())
        if key not in groups:
            groups[key] = []
        groups[key].append(node)

    commands = []
    for key, nodes in groups.items():
        if len(nodes) > 1:
            target_node = nodes[0]
            tags_to_merge = {}

            # Collect and merge tags using unicode-safe logic
            for node in nodes:
                tags = node.getInterestingTags()
                for k, v in tags.items():
                    if k not in tags_to_merge:
                        tags_to_merge[k] = set()
                    tags_to_merge[k].add(unicode(v))

            # Create the merged tag map
            new_tags = TagMap()
            for k, values in tags_to_merge.items():
                new_tags.put(k, u";".join(sorted(list(values))))

            # Create a clone of the target node and apply new tags
            updated_node = Node(target_node)
            updated_node.setKeys(new_tags)
            
            # Queue the tag change
            commands.append(ChangeCommand(target_node, updated_node))

            # Queue deletion of the redundant duplicates
            for i in range(1, len(nodes)):
                commands.append(DeleteCommand(nodes[i]))

    # 2. Execute as a single undoable action using the UndoRedoHandler singleton
    if commands:
        undo_handler = UndoRedoHandler.getInstance()
        undo_handler.add(SequenceCommand(u"Merge GeoJSON Nodes", commands))
        print(u"Success: Merged {} clusters of nodes.".format(len(commands)/2))
    else:
        print("No overlapping nodes found in the current selection.")
else:
    print("Error: No active data layer found. Please select your GeoJSON layer.")
