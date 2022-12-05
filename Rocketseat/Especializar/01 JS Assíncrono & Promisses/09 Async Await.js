const promessa = new Promise( function(resolve, reject) {
    return resolve("ok")
  })
  
  async function start() {
    try {
      const result = await promessa
      console.log(result)
    } catch (error) {
        console.log(error)
    } finally {
        console.log("Rodar sempre")
    }
  } 
  
  start()