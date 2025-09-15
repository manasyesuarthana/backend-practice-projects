import express from "express";
import {verifyJWT} from "../middlewares/authMiddleware.js";
import {postTask, updateTask, deleteTask, getTasks} from "../controllers/todoController.js";

const router = express.Router();

router.post("/", verifyJWT, postTask);
router.put("/:id", verifyJWT, updateTask);
router.delete("/:id", verifyJWT, deleteTask);
router.get("/", verifyJWT, getTasks);

export default router;