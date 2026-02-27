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

        # Build groups based on overlapping ref:gid values
        groups = []

        for node in selected_nodes:
            gid_value = node.get("ref:gid")
            if not gid_value:
                continue

            gid_set = set(gid_value.split(";"))

            merged_into_existing = False

            for group in groups:
                if gid_set & group["gid_values"]:
                    group["nodes"].append(node)
                    group["gid_values"].update(gid_set)
                    merged_into_existing = True
                    break

            if not merged_into_existing:
                groups.append({
                    "nodes": [node],
                    "gid_values": set(gid_set)
                })

        commands = []
        merged_count = 0

        for group in groups:
            nodes = group["nodes"]

            if len(nodes) > 1:

                # Prefer server node with lowest positive ID
                server_nodes = [n for n in nodes if not n.isNew()]

                if server_nodes:
                    target_node = min(server_nodes, key=lambda n: n.getId())
                else:
                    target_node = min(nodes, key=lambda n: n.getId())

                # Merge all tags (still using interesting tags as in your version)
                tags_to_merge = {}

                for node in nodes:
                    tags = node.getInterestingTags()
                    for k, v in tags.items():
                        tags_to_merge.setdefault(k, set()).add(unicode(v))

                # Properly merge ref:gid values
                tags_to_merge["ref:gid"] = group["gid_values"]

                new_tags = TagMap()
                for k, values in tags_to_merge.items():
                    new_tags.put(k, u";".join(sorted(values)))

                updated_node = Node(target_node)
                updated_node.setKeys(new_tags)

                commands.append(ChangeCommand(target_node, updated_node))

                for node in nodes:
                    if node != target_node:
                        commands.append(DeleteCommand(node))

                merged_count += 1

        if commands:
            undo_handler = UndoRedoHandler.getInstance()
            undo_handler.add(
                SequenceCommand(
                    u"Merge Nodes by ref:gid (Smart Multi-Value)",
                    commands
                )
            )
            print(u"Success: Merged {} ref:gid groups.".format(merged_count))
        else:
            print("No overlapping ref:gid values found among selected nodes.")

else:
    print("Error: No active data layer found.")