# Homework: Writing Your Research Paper

## Overview

Now that you have completed your initial data analysis, conducted preliminary literature review work, and developed research questions, it's time to begin writing your research paper. This assignment has three main components: structuring your repository professionally, automating your literature review workflow, and starting your LaTeX paper.

## Part 0: Structure Your Repository

### Objective

Organize your repository according to professional research project standards.

### Requirements

1. **Create a standard research repository structure**:
   ```
   your-project-name/
   ├── data/          # datasets and data files
   ├── src/           # analysis scripts and code
   ├── paper/         # the paper being written (LaTeX files)
   ├── literature/    # related papers being reviewed (PDFs)
   ├── prompts/       # AI agent workflows and prompt files
   ├── figures/       # generated visualizations
   ├── .gitignore     # specify files to ignore
   └── README.md      # project documentation
   ```

2. **Reorganize your existing files** into this structure:
   - Move analysis scripts/notebooks to `src/`
   - Move dataset files to `data/`
   - Move downloaded research papers to `literature/`
   - Move any generated plots/charts to `figures/`

3. **Create a `.gitignore` file** in your repository root:
   - Must prevent machine-generated files from being committed to git
   - **Exception**: PDFs and images should be committed (these are valuable outputs)
   - Should exclude LaTeX auxiliary files (`.aux`, `.log`, `.out`, `.bbl`, `.blg`, etc.)
   - Should exclude system files (`.DS_Store`, etc.)
   - Should exclude large data files if appropriate for your project

### Deliverable

A well-organized repository following the standard structure with an appropriate `.gitignore` file.

## Part 1: Create an AI Agent Workflow for Your Literature Review

### Objective

Create a `literature-review.prompt.md` file that automates the literature review process for **your specific project**.

### Requirements

1. **Create file**: `prompts/literature-review.prompt.md` in your repository

2. **Follow the structure taught in class**:
   - YAML frontmatter (type, version, author, created, description, prerequisites)
   - All standard sections: Overview, Input, Output, Instructions, Constraints, Expected Output Format, Verification

3. **Customize for YOUR project**:
   - What information do you need to extract that aligns with YOUR research questions?
   - What makes a paper relevant to YOUR specific topic?
   - What domain-specific resources should you check?

### Deliverable

A complete, actionable `.prompt.md` file customized for your research project (not just the generic template)

## Part 2: Start Your LaTeX Research Paper

I use the Latex Workshop Extension in Vscode/Cursor.

### Objective

Copy the provided LaTeX template to your repository and begin drafting your paper.

### Requirements

1. **Copy the template** from this repository to yours:
   - Copy the entire `paper/` folder from this course repo to your repository
   - The template includes all necessary structure and helpful comments

2. **Customize the template**:
   - Update author information in `main.tex`
   - Choose a working title for your paper
   - Replace placeholder text with your content

3. **Write initial content** (required for this assignment):
   - **Abstract** (draft): 150-250 words summarizing your research
   - **Introduction** (draft): 
     - Problem/question, importance, contributions, paper outline
     - Fill in your research questions in the enumerated list
   - **Related Work** (outline):
     - Organize by themes (use the subsection structure provided)
     - Add at least 3-5 key papers with `\cite{}`
   - **Methodology** (outline):
     - Describe your data, methods, why these choices
   - **Bibliography**: Add at least 5 relevant references to `references.bib`
   - **Target length**: Approximately 2-3 pages for the first draft

4. **Compile successfully**:
   - Must produce a PDF
   - See `paper/README.md` for compilation instructions

### Deliverable

- A `paper/` folder in your repository with:
  - Compilable LaTeX document producing a PDF
  - Approximately 2-3 pages of drafted content
  - At least 5 references in bibliography
  - All references properly cited in text

### Tips

- **Read `paper/README.md` first** - it has all compilation instructions
- **Use Overleaf** if local compilation is challenging
- **Follow the comments** in each .tex file - they guide you on what to write
- **Reference the analyzed paper** in `literature/literature-review.md` as a structural model
- **Compile frequently** to catch errors early

---

## Submission

**Due Date**: [To be announced]

**What to submit**:
1. Push to your repository:
   - `prompts/literature-review.prompt.md`
   - `paper/` folder with all LaTeX files
   
2. In your repository, create a new file `HOMEWORK.md` that includes:
   - Link to your `.prompt.md` file
   - Link to your compiled PDF (upload the PDF to your repo)
   - Brief reflection (2-3 paragraphs):
     - How did creating the AI workflow change your thinking about literature review?
     - What challenges did you encounter with LaTeX?
     - What are the next steps for your paper?

## Resources

### AI Workflows
- Example in this repository: `prompts/literature-review.prompt.md`
- Prompt engineering guides: [Anthropic Claude](https://docs.anthropic.com/claude/docs/prompt-engineering), [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)

### LaTeX
- [Overleaf](https://www.overleaf.com/) - Online LaTeX editor
- [LaTeX templates](https://www.overleaf.com/latex/templates)
- ACM template: [ACM SIGCONF template](https://www.acm.org/publications/proceedings-template)
- IEEE template: [IEEE templates](https://www.ieee.org/conferences/publishing/templates.html)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX) - Comprehensive guide

### Research Paper Writing
- "How to Write a Great Research Paper" - Microsoft Research
- The analyzed paper in `literature/literature-review.md` as a structural example
- Your institution's writing center

---

## Getting Help

- **LaTeX issues**: Start with Overleaf tutorials, Stack Exchange (tex.stackexchange.com)
- **Workflow design**: Look at the example and think about what makes sense for YOUR project
- **Writing questions**: Use office hours, writing center, or peer review
- **Technical problems**: Git issues, compilation errors - document what you tried before asking

---

## Learning Objectives

By completing this assignment, you will:
1. Understand how to automate research processes using AI workflows
2. Learn to structure and document reproducible research methods
3. Gain practical experience with LaTeX for academic writing
4. Begin synthesizing your research into a coherent narrative
5. Practice professional research communication

**Remember**: This is the beginning of your research paper, not the end. You'll iterate on both the workflow and the paper throughout the rest of the semester. The goal is to get a solid foundation in place.
