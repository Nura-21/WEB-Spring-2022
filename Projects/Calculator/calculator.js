let f = '';
let s = '';
let sign = '';
let finish = false;

const digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'];
const action = ['-', '+', 'X', '/'];

//Screen
const out = document.querySelector('.calc-screen p')

function clearAll(){
    f = '';
    s = '';
    sign = '';
    finish = false;
    out.textContent = 0;
}

function limitStr(str, n, symb) {
    if (!n && !symb) return str;
    symb = symb || '';
    return str.substr(0, n - symb.length) + symb;
}

document.querySelector('.ac').onclick = clearAll;

document.querySelector('.buttons').onclick = event => {
    //Not button
    if(!event.target.classList.contains('btn')) return;
    //AC
    if(event.target.classList.contains('ac')) return;
    out.textContent = '';
    
    //Getting button
    const key = event.target.textContent;

    // [0-9] or .
    if(digit.includes(key)){
        if(s === '' && sign === ''){
            if(f === '0'){
                if(key !== '0'){
                    f = limitStr(f, 8, '');
                    f += key;
                    console.log(f, s, sign);
                    out.textContent = f;
                }else{
                    f = key;
                    console.log(f, s, sign);
                    out.textContent = f;
                }
            }else{
                f = limitStr(f, 8, '');
                f += key;
                console.log(f, s, sign);
                out.textContent = f;
            }
        }else if(f !== '' && s !== '' && finish){
            s = key;
            // s = limitStr(s, 8, '');
            finish = false;
            out.textContent = s;
        }else{
            s = limitStr(s, 8, '');
            s += key;
            out.textContent = s;
        }
        console.log(f, s, sign);
        return;
    }

    //Operations
    if(action.includes(key)){
        sign = key;
        out.textContent = sign;
        console.log(f, s, sign);
        return;
    }

    // =
    if(key === '='){
        if(s === '') s = f;
        switch(sign){
            case '+':
                f = (+f) + (+s);
                f = +((+f).toFixed(3));
                break;
            case '-':
                f = f - s;
                f = +((+f).toFixed(3));
                break;
            case 'X':
                f = f * s;
                f = +((+f).toFixed(3));
                break;
            case '/':
                if (s === '0'){
                    out.textContent = "Ошибка";
                    f = '';
                    s = '';
                    sign = '';
                    return;
                }
                f = f / s;
                f = +((+f).toFixed(3));
                break
        }
        finish = true;
        out.textContent = f;
        console.log(f, s, sign);
    }

    if(key === '%'){
        f = f / 100;
        out.textContent = f;
        console.log(f, s, sign);
    }

    if(key === '+/-'){
        f = -f;
        out.textContent = f;
        console.log(f, s, sign);
    }
}