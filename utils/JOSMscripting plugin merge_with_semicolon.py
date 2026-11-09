from org.openstreetmap.josm.gui import MainApplication
from org.openstreetmap.josm.data.osm import Node, TagMap
from org.openstreetmap.josm.data import UndoRedoHandler
from org.openstreetmap.josm.command import ChangeCommand, DeleteCommand, SequenceCommand

# 1. Get the current edit layer
layer = MainApplication.getLayerManager().getEditLayer()

if layer and layer.data:
    # Use selection if available, otherwise process all nodes
    selected_nodes = layer.data.getSelectedNodes()
    if not selected_nodes:
        selected_nodes = layer.data.getNodes()

    groups = {}
    for node in selected_nodes:
        # Group by coordinates (5 decimal places)
        key = "{:.5f},{:.5f}".format(
            node.getCoor().lat(),
            node.getCoor().lon()
        )

        if key not in groups:
            groups[key] = []

        groups[key].append(node)

    commands = []
    merged_clusters = 0
    deleted_new_nodes = 0

    for key, nodes in groups.items():
        if len(nodes) > 1:

            # ---------------------------------------------------------
            # Find an existing OSM node (positive ID).
            # Existing nodes have id > 0.
            # New/imported nodes have id == 0.
            # ---------------------------------------------------------

            existing_nodes = [n for n in nodes if n.getId() > 0]
            new_nodes = [n for n in nodes if n.getId() == 0]

            # If there is no existing OSM node, keep the first new node
            # as the target and merge the others into it.
            if existing_nodes:
                target_node = existing_nodes[0]
            else:
                target_node = nodes[0]

            tags_to_merge = {}

            # ---------------------------------------------------------
            # Collect tags from all nodes
            # ---------------------------------------------------------

            for node in nodes:
                tags = node.getInterestingTags()

                for k, v in tags.items():
                    if k not in tags_to_merge:
                        tags_to_merge[k] = set()

                    tags_to_merge[k].add(unicode(v))

            # ---------------------------------------------------------
            # Create merged tag map
            # ---------------------------------------------------------

            new_tags = TagMap()

            for k, values in tags_to_merge.items():
                new_tags.put(
                    k,
                    u";".join(sorted(list(values)))
                )

            # ---------------------------------------------------------
            # Apply merged tags to target node
            # ---------------------------------------------------------

            updated_node = Node(target_node)
            updated_node.setKeys(new_tags)

            commands.append(
                ChangeCommand(target_node, updated_node)
            )

            # ---------------------------------------------------------
            # DELETE ONLY NEW NODES.
            #
            # Never delete an existing OSM node (id > 0).
            # ---------------------------------------------------------

            for node in new_nodes:
                if node != target_node:
                    commands.append(
                        DeleteCommand(node)
                    )
                    deleted_new_nodes += 1

            merged_clusters += 1

    # 2. Execute as one undoable action
    if commands:
        undo_handler = UndoRedoHandler.getInstance()

        undo_handler.add(
            SequenceCommand(
                u"Merge GeoJSON Nodes",
                commands
            )
        )

        print(
            u"Success: merged {} clusters, deleted {} new nodes. "
            u"Existing OSM nodes were preserved.".format(
                merged_clusters,
                deleted_new_nodes
            )
        )

    else:
        print("No overlapping nodes found in the current selection.")

else:
    print(
        "Error: No active data layer found. "
        "Please select your GeoJSON layer."
    )
