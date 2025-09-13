import dotenv from "dotenv";
import express from "express";
import routes from "./routes/index.js";
import connectDB from  "./config/db.js";
import cors from 'cors';

dotenv.config();
connectDB();

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));
app.use("/api", routes);

app.get("/", (req, res) =>{
    res.json({message: 'The Blog API is working properly!'})
});

app.listen(port, () =>{
    console.log(`Server running on port ${port}`);
});