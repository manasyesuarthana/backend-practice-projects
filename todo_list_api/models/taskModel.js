import mongoose from "mongoose";
import Counter from "./counter.js";

const taskSchema = new mongoose.Schema({
    id:{
        type: Number,
        unique: true
    },
    title:{
        type: String,
        required: true
    },
    description:{
        type: String,
        required: true
    },
    user:{
        type: mongoose.Schema.ObjectId,
        required: true,
        ref: "User"
    }
}, {
    timestamps: true
});

taskSchema.pre("save", async function(next) {
    if (this.isNew) {
        try {
            const counter = await Counter.findByIdAndUpdate(
                { _id: "taskId" },
                { $inc: { seq: 1 } },
                { new: true, upsert: true }
            );
            this.id = counter.seq;
            next();
        } catch (error) {
            next(error);
        }
    } else {
        next();
    }
});

export default mongoose.model("Task", taskSchema);