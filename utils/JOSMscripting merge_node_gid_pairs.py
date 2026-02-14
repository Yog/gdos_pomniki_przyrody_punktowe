from org.openstreetmap.josm.gui import MainApplication
from org.openstreetmap.josm.data.osm import Node, TagMap
from org.openstreetmap.josm.data import UndoRedoHandler
from org.openstreetmap.josm.command import ChangeCommand, DeleteCommand, SequenceCommand

layer = MainApplication.getLayerManager().getEditLayer()

if layer and layer.data:

    selected_nodes = layer.data.getSelectedNodes()

    if not selected_nodes:
        print("No nodes selected. Please select nodes first.")
    else:

        # Group nodes by ref:gid
        groups = {}
        for node in selected_nodes:
            gid = node.get("ref:gid")
            if gid:
                groups.setdefault(gid, []).append(node)

        commands = []
        merged_count = 0

        for gid, nodes in groups.items():
            if len(nodes) > 1:

                # Separate server and new nodes
                server_nodes = [n for n in nodes if not n.isNew()]

                if server_nodes:
                    # Keep server node with lowest positive ID
                    target_node = min(server_nodes, key=lambda n: n.getId())
                else:
                    # All nodes are new > keep lowest ID (closest to zero)
                    target_node = min(nodes, key=lambda n: n.getId())

                # Merge tags
                tags_to_merge = {}
                for node in nodes:
                    tags = node.getInterestingTags()
                    for k, v in tags.items():
                        tags_to_merge.setdefault(k, set()).add(unicode(v))

                new_tags = TagMap()
                for k, values in tags_to_merge.items():
                    new_tags.put(k, u";".join(sorted(values)))

                updated_node = Node(target_node)
                updated_node.setKeys(new_tags)

                commands.append(ChangeCommand(target_node, updated_node))

                # Delete all others
                for node in nodes:
                    if node != target_node:
                        commands.append(DeleteCommand(node))

                merged_count += 1

        if commands:
            undo_handler = UndoRedoHandler.getInstance()
            undo_handler.add(
                SequenceCommand(
                    u"Merge Nodes by ref:gid (Prefer OSM, Lowest ID)",
                    commands
                )
            )
            print(u"Success: Merged {} ref:gid groups.".format(merged_count))
        else:
            print("No duplicate ref:gid values found among selected nodes.")

else:
    print("Error: No active data layer found.")
