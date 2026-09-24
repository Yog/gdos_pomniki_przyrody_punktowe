from org.openstreetmap.josm.gui import MainApplication
from org.openstreetmap.josm.command import ChangePropertyCommand
from javax.swing import JOptionPane

layer = MainApplication.getLayerManager().getEditLayer()

converted = 0
skipped = 0
commands = []

if layer is None:
    JOptionPane.showMessageDialog(None, "No active OSM data layer.")
else:

    for primitive in layer.data.getSelected():
        value = primitive.get("circumference")

        if value is None:
            continue

        try:
            num = float(value)

            # Values >= 10 are centimetres
            if num >= 10:
                metres = num / 100.0

                # Keep sensible formatting
                new_value = ("%.2f" % metres).rstrip("0").rstrip(".")

                # Create a proper JOSM edit command
                commands.append(
                    ChangePropertyCommand(
                        primitive,
                        "circumference",
                        new_value
                    )
                )

                converted += 1

            else:
                skipped += 1

        except:
            print("Could not convert circumference: " + str(value))

    # Execute through JOSM's command system
    if commands:
        from org.openstreetmap.josm.command import SequenceCommand

        sequence = SequenceCommand(
            "Convert circumference from cm to m",
            commands
        )

        MainApplication.undoRedo.add(sequence)

    print("Converted: " + str(converted))
    print("Already in metres / skipped: " + str(skipped))

    JOptionPane.showMessageDialog(
        None,
        "Converted " + str(converted) +
        " circumference values from cm to m.\n" +
        str(skipped) +
        " values already in metres.\n\n" +
        "JOSM should now show these objects as modified."
    )
