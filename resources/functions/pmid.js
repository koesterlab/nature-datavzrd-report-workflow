function pmid(value) {
    const pmidRegex = /PMID:\s*(\d+)/;
    const match = value.match(pmidRegex);

    if (match) {
        const pmidNumber = match[1];
        return `<a href="https://pubmed.ncbi.nlm.nih.gov/${pmidNumber}/" target="_blank">${pmidNumber}</a>`;
    } else {
        return value;  // Return the original value if no valid PMID is found
    }
}