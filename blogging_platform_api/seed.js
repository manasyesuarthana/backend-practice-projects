import mongoose from 'mongoose';
import bcrypt from 'bcrypt';
import dotenv from 'dotenv';
import User from './models/userModel.js';

// Load environment variables
dotenv.config();

const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI);
        console.log('MongoDB connected for seeding...');
    } catch (error) {
        console.error(`Error connecting to MongoDB: ${error}`);
        process.exit(1);
    }
};

const seedAdmin = async () => {
    try {
        await connectDB();

        // Check if admin user already exists
        const adminExists = await User.findOne({ username: process.env.ADMIN_USERNAME });

        if (adminExists) {
            console.log('Admin user already exists. Seeding skipped.');
            return;
        }

        // Hash the admin password
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(process.env.ADMIN_PASSWORD, salt);

        // Create the admin user
        const adminUser = new User({
            username: process.env.ADMIN_USERNAME,
            password: hashedPassword,
            role: 'admin', // Explicitly set the role to 'admin'
        });

        await adminUser.save();
        console.log('✅ Admin user created successfully!');

    } catch (error) {
        console.error('Error seeding the database:', error);
    } finally {
        // Ensure the database connection is closed
        mongoose.disconnect();
        console.log('MongoDB connection closed.');
    }
};

seedAdmin();