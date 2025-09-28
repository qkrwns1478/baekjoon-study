const solution = (code) => {
    let ret = '';
    let mode = 0;
    
    for (let i = 0; i < code.length; i++) {
        if (code[i] === "1") {
            mode = !mode;
        } else if (mode && i % 2) {
            ret += code[i];
        } else if (!mode && !(i % 2)) {
            ret += code[i];
        }
    }
    return ret || "EMPTY";
}