import User from "../models/userModel.js";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";


export const registerPage = (req, res) => {
    res.render("register");
};
export const loginPage = (req, res) => {
    res.render("login");
};

export const registerUser = async (req, res) => {
    const {name, email, password} = req.body;

    try{
        const userExists = await User.findOne({email});
        if(userExists){
            return res.status(400).json({error: "Email already taken. Please use a different one."});
        }

        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const user = new User({name, email, password: hashedPassword});
        await user.save();
        res.status(201).json({message: "User registered sucessfully."});
    }

    catch(error){
        console.error(error);
        res.status(500).json({error: "User registration failed."});
    }
};

export const loginUser = async (req, res) => {
    const {email, password} = req.body;
    try{
        const user = await User.findOne({email});

        if(user && (await bcrypt.compare(password, user.password))){
            const token = jwt.sign(
                {
                    userId: user._id,
                },
                process.env.JWT_SECRET,
                {expiresIn: "1h"}
            );

            res.status(200).json({
                message: "Login Sucessful.",
                token: token
            });
        }
        else{
            return res.status(401).json({error: "Invalid email or password."});
        }
    }
    catch(error){
        console.error(error);
        res.status(500).json({error: "Login Failed."});
    }
};