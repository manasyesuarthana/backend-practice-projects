import jwt from "jsonwebtoken";
import User from "../models/userModel.js";

export const verifyJWT = async (req, res, next) =>{
    if(!req.headers.authorization || !req.headers.authorization.startsWith('Bearer')){
        return res.status(401).json({error: 'Not authorized. No token found.'});
    }

    try{
        //get token from header (e.g., "Bearer eyJhbGci...")
        const token = req.headers.authorization.split(' ')[1];

        const decoded = jwt.verify(token, process.env.JWT_SECRET);

        req.user = await User.findById(decoded.userId).select("-password");
        
        if(!req.user){
            return res.status(401).json({error: 'Not authorized. User not found.'});
        }

        next();
    }
    catch(error){
        return res.status(401).json({error: 'Not authorized: Token is invalid.'});
    }
};