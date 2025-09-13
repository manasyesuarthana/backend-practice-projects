import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import User from "../models/userModel.js";

export const registerPage = async (req, res) =>{
    res.render("register");
};

export const registerUser = async (req, res) =>{
    const {username, password} = req.body;

    try{
        const userExists = await User.findOne({username});
        if(userExists){
            return res.status(400).json({error:'User already exists.'});
        }
        
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const user = new User({username, password: hashedPassword});
        await user.save();

        res.status(201).json({message: 'User registered sucessfully.'});
    }
    catch(error){
        res.status(500).json({error:'Registration Failed.'});
        console.error(error);
    }
}

export const loginPage = (req, res) =>{
    res.render("login");
}

export const loginUser = async (req, res) => {
    try{
        const {username, password} = req.body;
        
        const user = await User.findOne({username});

        if(user && (await bcrypt.compare(password, user.password))){
            const token = jwt.sign(
                {
                    userId: user._id, 
                    role: user.role
                },
                process.env.JWT_SECRET,
                {expiresIn: '1h'}
            );

            res.status(200).json({
                message: 'Login successful.',
                token: token
            });
        }
        else{
            res.status(401).json({error:'Invalid username or password'});
        }
    }
    catch(error){
        res.status(500).json({error:'Login Failed.'});
        console.error(error);
    }

}