const path = require("path")
const HtmlWebpackPlugin = require("html-webpack-plugin")

module.exports = {
    mode: "development",
    // entry - caminho do arquivo principal/inicial
    entry: path.resolve(__dirname, "src", "index.jsx"),

    // Arquivo que eu vou gerar com o webpack
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js"

    },

    resolve: {
        extensions: [".js", ".jsx"]
    },

    devServer: {
        // Aonde está noso arquivo html com o conteúdo estático da aplicação
        contentBase: path.resolve(__dirname, "public"),
    },

    plugins: [
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, "public", "index.html")
        })
    ],

    // Como nossa aplicação vai se comportar quando eu estiver importando diferentes tipos de arquivos
    module: {
        rules: [
            // O que eu to fazendo é importando um arquivo jsx, e preciso converter ele usando o babel
            {  
                test: /\.jsx$/,
                exclude: /node_modules/,
                use: "babel-loader"
            }
        ],
    }
}