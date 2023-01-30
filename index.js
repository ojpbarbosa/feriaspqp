const express = require("express");

const app = express();
const port = process.env.PORT || 3030;

app.get("/", (request, response) => response.send("twilightime"));

app.listen(port);
