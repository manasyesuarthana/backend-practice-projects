import express from "express";
import auth from "./authRoutes.js";
import todos from "./todoRoutes.js";

const router = express.Router();

router.use("/auth", auth);
router.use("/todos", todos);

export default router;