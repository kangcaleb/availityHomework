const parenthesesChecker = (string) => {

    const stack = [];
    for(let i=0; i<string.length; i++) {
        const char = string.charAt(i);

        if (char == '(') {
            stack.push(char);
        } else if (char == ')') {
            const removed = stack.pop();
            if (removed === undefined) {
                return false;
            }
        }
    }

    return stack.length == 0;
}

console.log(parenthesesChecker(   "[()]{}{[()()]()}"  ));