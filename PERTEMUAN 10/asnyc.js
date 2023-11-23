async function get(){
    setTimeout(() => {
        return "aaaa"
    }, 0);
}

const getData = async () => {
    let response = 0
    setTimeout(() => {
       response = "aaaa"
    }, 1000);
    // const data = await response.json();
    return response;
    
}

// console.log(getData());

async function get2(){
    const data = await getData()
    console.log(data)

}

get2()