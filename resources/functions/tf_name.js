function tf_name(value) {
    const items = value
        .replace(/[\[\]']/g, '')
        .split(',')
        .map(item => item.trim())
        .sort();

    return items.map(item =>
        `<span style="display: inline-block; padding: 5px 10px; margin: 5px; background-color: grey; color: white; border-radius: 15px;">${item}</span>`
    ).join('');
}