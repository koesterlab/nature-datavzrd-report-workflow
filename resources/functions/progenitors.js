function progenitors(value) {
    const colorMap = {
        "Ectoderm": { color: "lightblue", textColor: "black" },
        "Mesoderm": { color: "lightcoral", textColor: "black" },
        "Neural crest": { color: "lightseagreen", textColor: "white" },
        "Mesenchyme": { color: "lightgoldenrodyellow", textColor: "black" },
        "Surface ectoderm": { color: "lightpink", textColor: "black" },
        "Epidermis": { color: "lightskyblue", textColor: "black" },
        "Mucosal epithelium": { color: "lavender", textColor: "black" },
        "Dermomyotome": { color: "lightgreen", textColor: "black" },
        "Brain": { color: "lightsteelblue", textColor: "black" },
        "AGM": { color: "lightyellow", textColor: "black" },
        "Urogenital ridge": { color: "palevioletred", textColor: "white" },
        "Branchial arch": { color: "lightgrey", textColor: "black" },
        "Sclerotome": { color: "peachpuff", textColor: "black" },
        "Notochord": { color: "plum", textColor: "white" },
        "Connective tissue": { color: "lightcyan", textColor: "black" },
        "Cartilage primordium": { color: "wheat", textColor: "black" },
        "Endoderm": { color: "palegreen", textColor: "black" },  // Kept distinct
        "Primitive gut tube": { color: "mediumseagreen", textColor: "white" },
        "Pancreas primordium": { color: "red", textColor: "white" },
        "Lung primordium": { color: "pink", textColor: "black" },
        "Mesothelium": { color: "lightblue", textColor: "black" },
        "Smooth muscle": { color: "lightgreen", textColor: "black" },
        "Cartilage": { color: "lightyellow", textColor: "black" },
        "Head mesenchyme": { color: "coral", textColor: "white" }
    };

    const progenitorsList = value.split(',').map(item => item.trim());
    const pills = progenitorsList.map(progenitor => {
        const { color, textColor } = colorMap[progenitor] || { color: 'gray', textColor: 'black' };
        return `<span style="display: inline-block; padding: 5px 10px; margin: 5px; background-color: ${color}; color: ${textColor}; border-radius: 15px;">${progenitor}</span>`;
    });

    return pills.join('');
}
