import express from "express";
import {getAllBlogs, getSpecificBlog, postBlog, deleteBlog, editBlog} from "../controllers/blogController.js";
import {verifyToken, isAdmin} from "../middlewares/authMiddleware.js";

const router = express.Router();

router.get("/", getAllBlogs);
router.get("/:id", getSpecificBlog);

router.post("/", verifyToken, isAdmin, postBlog);
router.delete("/:id", verifyToken, isAdmin, deleteBlog);
router.put("/:id", verifyToken, isAdmin, editBlog);

export default router;