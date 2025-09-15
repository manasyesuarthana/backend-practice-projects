import Task from "../models/taskModel.js";

export const postTask = async (req, res) => {
    const {title, description} = req.body;

    try{
        const newTask = new Task({
            title: title,
            description: description,
            user: req.user._id
        });
        const savedTask = await newTask.save();
        res.status(201).json(savedTask);
    }
    catch(error){
        console.error(error);
        res.status(500).json({error: "Failed to save task."});
    }
};

export const updateTask = async (req, res) => {
    const id = req.params.id;
    const {title, description} = req.body;

    try{
        const task = await Task.findOneAndUpdate(
            {id: id, user: req.user._id},
            {title, description},
            {new: true, runValidators: true}
        );

        if(!task){
            return res.status(404).json({error: "Task with specified ID not found."});
        }

        res.status(200).json(task);

    }
    catch(error){
        console.error(error);
        res.status(500).json({error: "Failed to update task."});
    }
};

export const deleteTask = async (req, res) => {
    const id = req.params.id;
    
    try{
        const deletedTask = await Task.findOneAndDelete({id: id, user: req.user._id})
        if(!deletedTask){
            return res.status(404).json({error: "Task with specified ID not found."});
        }
        res.status(200).json({message: "Task deleted sucessfully."});
    }
    catch(error){
        console.error(error);
        res.status(500).json({error: "Failed to delete task."});
    }
};

export const getTasks = async (req, res) => {
    const page = req.query.page; //page
    const limit = req.query.limit; //limit of tasks per page
    const skip = (page - 1) * limit;

    try{
        const tasks = await Task.find({user: req.user._id})
            .sort({createdAt: -1})
            .skip(skip)
            .limit(limit);

        const totalTasks = await Task.countDocuments({user: req.user._id});

        res.status(200).json({
            tasks,
            currentPage: page,
            limit: limit,
            totalPages: Math.ceil(totalTasks / limit)
        });
    }
    catch(error){
        console.error(error);
        res.status(500).json({error: "Failed retrieving tasks."});
    }
};