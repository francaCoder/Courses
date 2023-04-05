module.exports = {
    // runtime serve para não termos que importar o react em todo arquivo .jsx
    presets: [
        "@babel/preset-env",
        ["@babel/preset-react", {
            runtime: "automatic"
        }]
    ]
}