import express from "express";
import {loginUser, registerUser, loginPage, registerPage} from "../controllers/authController.js";
const router = express.Router();

router.get("/login", loginPage);
router.get("/register", registerPage);
router.post("/login", loginUser);
router.post("/register", registerUser);

export default router;