import express from "express";
import {registerUser, loginUser, loginPage, registerPage} from "../controllers/authController.js";

const router = express.Router();

router.get("/login", loginPage);
router.get("/register", registerPage)
router.post("/register", registerUser);
router.post("/login", loginUser);

export default router;  