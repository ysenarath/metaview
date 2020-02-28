'use strict'

const path = require('path');

const {VueLoaderPlugin} = require('vue-loader');

module.exports = {
    entry: './src/app.js',
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, '../static')
    },
    plugins: [
        new VueLoaderPlugin()
    ]
};
