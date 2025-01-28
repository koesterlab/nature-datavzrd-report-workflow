function genePills(value) {
    const colorMap = {
        "Reep5": { color: "#FF6347", textColor: "white" },
        "Cpa1": { color: "#32CD32", textColor: "white" },
        "Cel": { color: "#1E90FF", textColor: "white" },
        "Rbpjl": { color: "#FFD700", textColor: "black" },
        "Ptf1a": { color: "#8A2BE2", textColor: "white" },
        "Mki67": { color: "#FF1493", textColor: "white" },
        "Kif11": { color: "#00FA9A", textColor: "black" },
        "Ccdc34": { color: "#DC143C", textColor: "white" },
        "Bicc1": { color: "#FF4500", textColor: "black" },
        "Sox9": { color: "#2E8B57", textColor: "white" },
        "Anxa2": { color: "#D2691E", textColor: "white" },
        "Spp1": { color: "#F4A460", textColor: "black" },
        "Nav2": { color: "#8B0000", textColor: "white" },
        "Cadm1": { color: "#6A5ACD", textColor: "white" },
        "Neurog3 (low)": { color: "#A52A2A", textColor: "white" },
        "Gadd45a": { color: "#ADFF2F", textColor: "black" },
        "Btbd17": { color: "#B22222", textColor: "white" },
        "Hes6": { color: "#9932CC", textColor: "black" },
        "Neurog3 (high)": { color: "#8B008B", textColor: "white" },
        "Fev": { color: "#FF8C00", textColor: "white" },
        "Cck": { color: "#FFD700", textColor: "black" },
        "Vwa5b2": { color: "#C71585", textColor: "white" },
        "Tox3": { color: "#4B0082", textColor: "white" },
        "Neurod1": { color: "#0000CD", textColor: "white" },
        "Hhex": { color: "#FF6347", textColor: "white" },
        "Dctn3": { color: "#32CD32", textColor: "black" },
        "Yipf4": { color: "#1E90FF", textColor: "white" },
        "Ppp3ca": { color: "#FFD700", textColor: "black" },
        "Pclo": { color: "#8A2BE2", textColor: "white" },
        "Ubl3": { color: "#FF1493", textColor: "white" },
        "Arx": { color: "#00FA9A", textColor: "black" },
        "Zwint": { color: "#DC143C", textColor: "white" },
        "Npepl1": { color: "#FF4500", textColor: "black" },
        "Cox7a2l": { color: "#2E8B57", textColor: "white" },
        "Gcg": { color: "#D2691E", textColor: "black" },
        "Ins2": { color: "#F4A460", textColor: "white" },
        "Sst": { color: "#8B0000", textColor: "white" },
        "Ghrl": { color: "#6A5ACD", textColor: "black" }
    };

    const genesList = value.split(',').map(item => item.trim());
    const pills = genesList.map(gene => {
        const { color, textColor } = colorMap[gene] || { color: 'gray', textColor: 'black' };
        return `<span style="display: inline-block; padding: 5px 10px; margin: 5px; background-color: ${color}; color: ${textColor}; border-radius: 15px; cursor: pointer; transition: background-color 0.3s ease;">
                    <a href="https://www.genecards.org/cgi-bin/carddisp.pl?gene=${gene}" target="_blank" style="color: ${textColor}; text-decoration: none;">${gene}</a>
                </span>`;
    });

    return pills.join('');
}