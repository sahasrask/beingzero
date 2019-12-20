const express = require('express')
const app = express()
const port = 3000

app.use(express.static('frontend'))
var student = {"name" : "Being Zero",
               "college" : "VNRVJIET",
               "regno": "112323232"}

app.get('/', (req, res) => res.sendfile(__dirname+'/frontend/html/home.html'))
app.get('/login', (req, res) => res.send('login'))
app.get('/register', (req, res) => res.send('register'))
app.get('/data',(req,res)=>res.json(student))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))