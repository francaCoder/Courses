fetch("https://api.github.com/users/maykbrito").then(response => {
    response.json().then(data => fetch(data.repos_url)).then(res => res.json()).then(d => console.log(d))
})