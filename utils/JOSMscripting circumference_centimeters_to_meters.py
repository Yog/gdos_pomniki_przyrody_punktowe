from org.openstreetmap.josm.gui import MainApplication
from javax.swing import JOptionPane

converted = 0
skipped = 0

layer_manager = MainApplication.getLayerManager()

for layer in layer_manager.getLayers():
    if not hasattr(layer, "data"):
        continue

    for primitive in layer.data.allPrimitives():
        value = primitive.get("circumference")

        if value is None:
            continue

        try:
            num = float(value)

            # 10 or more = centimetres
            # Below 10 = already metres
            if num >= 10:
                metres = num / 100.0

                # Remove unnecessary trailing zeros
                new_value = ("%.2f" % metres).rstrip("0").rstrip(".")

                primitive.put("circumference", new_value)
                converted += 1
            else:
                skipped += 1

        except:
            print("Could not convert circumference: " + str(value))

print("Converted: " + str(converted))
print("Already in metres / skipped: " + str(skipped))

JOptionPane.showMessageDialog(
    None,
    "Converted " + str(converted) +
    " circumference values from cm to m.\n" +
    str(skipped) +
    " values left unchanged."
)
