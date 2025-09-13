import express from "express";
const router = express.Router();
import auth from "./authRoutes.js";
import blog from "./blogRoutes.js";
import {verifyToken, isAdmin} from "../middlewares/authMiddleware.js";
import Blog from "../models/blogModel.js";

router.use("/auth", auth);
router.use("/blog", blog);

router.get("/admin", verifyToken, isAdmin, async (req, res) => {
    try {
        const blogs = await Blog.find({})
            .populate('author', 'username')
            .sort({ createdAt: -1 });
        
        res.json({
            blogs,
            flag: process.env.flag,
            user: {
                id: req.user._id,
                username: req.user.username,
                role: req.user.role
            }
        });
    } catch (error) {
        res.status(500).json({ error: 'Error fetching admin data' });
    }
});

export default router;