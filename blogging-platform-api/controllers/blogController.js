import Blog from "../models/blogModel.js";

export const getAllBlogs = async (req, res) => {
    try{
        const blogs = await Blog.find({})
        .populate('author', 'username')
        .sort({createdAt: -1});
    
    res.status(200).json(blogs);
    }
    catch(error){
        res.status(500).json({error :'Error fetching blogs.'});
    }
};

export const getSpecificBlog = async (req, res) => {
    try{
        const blog = await Blog.findById(req.params.id)
        .populate('author', 'username');

        if(!blog){
            return res.status(404).json({error: 'Blog not found.'});
        }
        else{
            res.status(200).json(blog);
        }
    }
    catch(error){
        res.status(500).json({error: 'Error fetching blog.'})
    }
};

export const postBlog = async (req, res) => {
    try{
        const {title, content} = req.body;

        if(!title || !content){
            return res.status(400).json({error: 'Both title and content must be filled.'});
        }

        const newBlog = new Blog({
            title,
            content, 
            author: req.user._id
        });

        const savedBlog = await newBlog.save();
        res.status(201).json(savedBlog);
    }
    catch(error){
        res.status(500).json({error: 'Error creating blog post.'});
    }
};

export const editBlog = async (req, res) => {
    try{
        const {title, content} = req.body;

        const blog = await Blog.findById(req.params.id);
        if(!blog){
            return res.status(404).json({error: 'Blog post not found.'});
        }

        blog.title = title || blog.title;
        blog.content = content || blog.content;
        
        const updatedBlog = await blog.save();
        res.status(200).json(updatedBlog);
    }
    catch(error){
        res.status(500).json({error: 'Error updating/editing blog post.'});
    }
};


export const deleteBlog = async (req, res) => {
    try{
        const blog = await Blog.findById(req.params.id);

        if(!blog){
            return res.status(404).json({error: 'Blog post not found.'});
        }

        const isAdmin = req.user.role === 'admin';

        if(!isAdmin){
            return res.status(403).json({error: 'Not authorized.'});
        }

        await Blog.findByIdAndDelete(req.params.id);
        res.status(200).json({message: 'Blog successfully deleted.'});
    }
    catch(error){
        res.status(500).json({error: 'Error deleting blog post.'})
    }
};
