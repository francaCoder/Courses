// fetch("https://api.github.com/users/maykbrito")
// .then(response => response.json())
// .then(data => fetch(data.repos_url))
// .then(res => res.json()) 
// .then(d => console.log(d))
// .catch(err => console.log(err.message))

async function start() {
    try {
      const response = await fetch("https://api.github.com/users/maykbrito")
      const user = await response.json()
      const reposResponse = await fetch(user.repos_url)
      const repos = await reposResponse.json()
      console.log(repos)
    } catch (e) {
      console.log(e)
    }
  }
  
  start()