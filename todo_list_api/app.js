import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import bodyParser from "body-parser"; 
import routes from "./routes/index.js";
import connectDB from "./config/db.js";

dotenv.config();
connectDB();

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.use("/", routes);

app.get("/", (req, res) =>{
    res.json({message: "Welcome to the To-Do list API. Please refer to the documentation for usage."});
});

app.listen(port, () =>{
    console.log(`API running on port ${port}.`);
});