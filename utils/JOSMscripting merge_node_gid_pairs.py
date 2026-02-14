from org.openstreetmap.josm.gui import MainApplication
from org.openstreetmap.josm.data.osm import Node, TagMap
from org.openstreetmap.josm.data import UndoRedoHandler
from org.openstreetmap.josm.command import ChangeCommand, DeleteCommand, SequenceCommand

# Get current edit layer
layer = MainApplication.getLayerManager().getEditLayer()

if layer and layer.data:

    selected_nodes = layer.data.getSelectedNodes()

    if not selected_nodes:
        print("No nodes selected. Please select nodes first.")
    else:

        # Group nodes by ref:gid value
        groups = {}

        for node in selected_nodes:
            gid = node.get("ref:gid")
            if gid:
                if gid not in groups:
                    groups[gid] = []
                groups[gid].append(node)

        commands = []
        merged_count = 0

        for gid, nodes in groups.items():
            if len(nodes) > 1:

                # ?? Prefer OSM server node (isNew() == False)
                nodes_sorted = sorted(nodes, key=lambda n: n.isNew())
                target_node = nodes_sorted[0]

                tags_to_merge = {}

                # Merge tags from all nodes
                for node in nodes:
                    tags = node.getInterestingTags()
                    for k, v in tags.items():
                        if k not in tags_to_merge:
                            tags_to_merge[k] = set()
                        tags_to_merge[k].add(unicode(v))

                # Create merged tag map
                new_tags = TagMap()
                for k, values in tags_to_merge.items():
                    new_tags.put(k, u";".join(sorted(values)))

                # Clone and update target node
                updated_node = Node(target_node)
                updated_node.setKeys(new_tags)

                commands.append(ChangeCommand(target_node, updated_node))

                # Delete all other nodes except the chosen target
                for node in nodes:
                    if node != target_node:
                        commands.append(DeleteCommand(node))

                merged_count += 1

        if commands:
            undo_handler = UndoRedoHandler.getInstance()
            undo_handler.add(SequenceCommand(u"Merge Nodes by ref:gid (Prefer OSM)", commands))
            print(u"Success: Merged {} ref:gid groups.".format(merged_count))
        else:
            print("No duplicate ref:gid values found among selected nodes.")

else:
    print("Error: No active data layer found.")
