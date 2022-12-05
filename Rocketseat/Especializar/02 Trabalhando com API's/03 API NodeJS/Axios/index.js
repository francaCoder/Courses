const express = require('express')
const axios = require('axios')
const app = express()

app.listen("3000")

app.route("/").get((req, res) => {
    async function getUser() {
        try {
            const user = await axios.get("https://api.github.com/users/jakeliny")

            console.log(user.data.login)
        } catch (error) {
            console.log(error)
        }
    }

    getUser()
})