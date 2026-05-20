import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# Create workbook and setup sheets
wb = openpyxl.Workbook()

# Remove default sheet
default_sheet = wb.active
wb.remove(default_sheet)

# Sheet 1: Course Dashboard / Overview
ws_dash = wb.create_sheet(title="Course Overview")
ws_dash.views.sheetView[0].showGridLines = True

# Sheet 2: Exhaustive Syllabus Plan
ws_plan = wb.create_sheet(title="Exhaustive Syllabus")
ws_plan.views.sheetView[0].showGridLines = True

# Define Color Palette (Modern Executive Slate/Steel Blue Theme)
primary_color = "2B3E50"    # Dark Slate Blue for Primary Headers
accent_color = "4A90E2"     # Vibrant Slate Blue for Subheaders / Accents
zebra_color = "F4F7F9"      # Very Light cool grey for rows
text_light = "FFFFFF"       # White text
text_dark = "1C2833"        # Near black text
border_color = "D1D5DB"     # Soft light grey for cell dividers

font_title = Font(name="Segoe UI", size=16, bold=True, color=primary_color)
font_section = Font(name="Segoe UI", size=13, bold=True, color=text_light)
font_header = Font(name="Segoe UI", size=11, bold=True, color=text_light)
font_bold_data = Font(name="Segoe UI", size=11, bold=True, color=text_dark)
font_body = Font(name="Segoe UI", size=11, bold=False, color=text_dark)
font_italic = Font(name="Segoe UI", size=10, italic=True, color="555555")

fill_primary = PatternFill(start_color=primary_color, end_color=primary_color, fill_type="solid")
fill_accent = PatternFill(start_color=accent_color, end_color=accent_color, fill_type="solid")
fill_zebra = PatternFill(start_color=zebra_color, end_color=zebra_color, fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color=border_color),
    right=Side(style='thin', color=border_color),
    top=Side(style='thin', color=border_color),
    bottom=Side(style='thin', color=border_color)
)

# ----------------- POPULATE OVERVIEW DASHBOARD -----------------
ws_dash["A2"] = "Masterclass Blueprint: Ultimate AI-Driven Automation & QA Engineer"
ws_dash["A2"].font = font_title
ws_dash.row_dimensions[2].height = 25

overview_text = (
    "Welcome to your Comprehensive Udemy-Style Training Curriculum Map.\n\n"
    "This master program bridges the structural gap between foundational prompt engineering, "
    "enterprise software test design acceleration, and highly sophisticated multi-agent AI ecosystems.\n"
    "It merges production-level frameworks (Selenium, Playwright, Cypress) with deep engineering layers "
    "such as the Model Context Protocol (MCP), vector stores (RAG workflows), LLM unit testing (DeepEval), "
    "and self-healing infrastructure loops."
)
ws_dash["A4"] = overview_text
ws_dash["A4"].font = font_body
ws_dash["A4"].alignment = Alignment(wrap_text=True, vertical="top")
ws_dash.merge_cells("A4:F8")
ws_dash.row_dimensions[4].height = 20

# Overview Metadata Grid
metadata = [
    ("Metric / Parameter", "Value / Scope", "Strategic Objective"),
    ("Target Professional Role", "AI Automation Engineer / Principal QA Lead", "Transition from manual script creation to system orchestrators."),
    ("Total Core Course Sections", "5 Structural Milestone Sections", "Logical cognitive scaffolding maximizing framework retention."),
    ("Total Production Lectures", "33 High-Fidelity Deliverable Lectures", "Granular mapping from introductory tokens to advanced system nodes."),
    ("Hands-On Coding Portfolios", "4 Comprehensive Enterprise Assignments", "Ensures immediate script execution capability via clean design patterns."),
    ("Advanced Capstone Engines", "3 Multi-Agent Production Systems", "End-to-End deployment vectors designed to populate your engineering portfolio.")
]

row_idx = 10
for i, item in enumerate(metadata):
    ws_dash.row_dimensions[row_idx].height = 24
    for j, val in enumerate(item):
        cell = ws_dash.cell(row=row_idx, column=j+1, value=val)
        if i == 0:
            cell.font = font_header
            cell.fill = fill_primary
            cell.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell.font = font_bold_data if j == 0 else font_body
            cell.border = thin_border
            cell.alignment = Alignment(wrap_text=True, vertical="center")
            if i % 2 == 0:
                cell.fill = PatternFill(start_color="EAECEE", end_color="EAECEE", fill_type="solid")
    row_idx += 1

# ----------------- POPULATE EXHAUSTIVE SYLLABUS -----------------
headers = ["Lecture ID", "Lecture Title", "Instructional Type", "Core Architectural Concepts", "Implementation Details / Deliverables", "Target Tools / Infrastructure"]

# Setup main table headers
ws_plan.row_dimensions[1].height = 28
for col_num, header in enumerate(headers, 1):
    cell = ws_plan.cell(row=1, column=col_num, value=header)
    cell.font = font_header
    cell.fill = fill_primary
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Complete syllabus dataset mapped across the 5 structural sections
syllabus_data = [
    # SECTION 1
    {"section": "Section 1: Generative AI Fundamentals & The Prompt Engineering Sandbox"},
    {"id": "L-01", "title": "Course Introduction & The Shift-Left AI Testing Revolution", "type": "Video (Theory)", "concepts": "Evolution of QA paradigms; manual vs automated vs autonomous testing thresholds; context window economy.", "impl": "Establish local study parameters; map traditional test suite friction metrics to AI metrics.", "tools": "AI Glossaries, Program Architecture Blueprint Maps"},
    {"id": "L-02", "title": "Demystifying LLMs: Tokens, Context Windows, and Neural Reasoning", "type": "Video (Theory)", "concepts": "Mechanics of deep learning frameworks; tokenization weights; how transformers compute probabilistic next-tokens.", "impl": "Analyze semantic drift examples and multi-paragraph window optimization behaviors.", "tools": "Tokenization Calculators, Core LLM Architectures"},
    {"id": "L-03", "title": "Architecture Showdown: Commercial vs. Open-Source Models", "type": "Video + Demo", "concepts": "Enterprise data compliance boundaries; comparison matrices of closed source models vs open open source instances.", "impl": "Construct an evaluation matrices matrix matching cost, safety, context depth, and accuracy requirements.", "tools": "GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, DeepSeek-V3"},
    {"id": "L-04", "title": "Setting Up Your Private QA Lab: Ollama & LM Studio", "type": "Code-Along", "concepts": "Local model compilation; hosting offline infrastructure pipelines to prevent data leakage of proprietary test configurations.", "impl": "Compile local runtimes of Mistral and DeepSeek models; verify OpenAI-compatible local endpoints.", "tools": "Ollama CLI, LM Studio Core Engine, Mistral, DeepSeek OSS"},
    {"id": "L-05", "title": "Prompt Engineering Foundations: Zero-Shot vs. Few-Shot Inferences", "type": "Video + Practice", "concepts": "Context manipulation; conditioning behavioral weight variables through historical message state arrays.", "impl": "Code baseline text patterns to parse complex acceptance criteria without model hallucination.", "tools": "ChatGPT UI, Claude Workbench Sandbox"},
    {"id": "L-06", "title": "Enterprise QA Prompting Frameworks: STAR, CLEAR, and CRISP", "type": "Video + Interactive", "concepts": "Structural taxonomy models for prompt execution; systematic context generation via markdown config states.", "impl": "Assemble reusable text payload structures using structured schema syntax templates.", "tools": "Markdown Layout Frameworks (.md), Prompt Repositories"},
    {"id": "L-07", "title": "Deep Dive: The RICE POT Framework for Software Testers", "type": "Video + Workbook", "concepts": "Advanced tactical role assignment matrices customized explicitly for system evaluation engineers.", "impl": "Execute edge-case boundary conditions parsing using precise target criteria.", "tools": "RICE POT Formal Specifications, Prompt Asset Files"},
    {"id": "A-01", "title": "Section Assignment: The Markdown Prompt Engineering Suite", "type": "Hands-On Coding", "concepts": "Combining Markdown contexts and few-shot structural logic to output programmatic schemas.", "impl": "Deliverable: Compile an optimized prompt payload asset parsing dynamic stories into boundary logic objects.", "tools": "IDE Editor, JSON Validation Schemas"},
    
    # SECTION 2
    {"section": "Section 2: AI-Powered Test Artifacts & Smart Strategy Generation"},
    {"id": "L-08", "title": "Requirements Deconstruction & Ambiguity Analysis via AI", "type": "Video + Demo", "concepts": "Automated logic mapping; scanning business profiles for syntax conflicts, missing boundaries, or logic holes.", "impl": "Import unstructured enterprise specifications and extract isolated technical execution prerequisites.", "tools": "Jira Agile User Stories, LLM Parsing Engines"},
    {"id": "L-09", "title": "Generating Complete Test Plans & Shift-Left Strategies", "type": "Code-Along", "concepts": "Algorithmic estimations; dynamic risk analysis scoping matrices; defining strategic entry and exit parameters.", "impl": "Produce an enterprise-ready testing plan detailing dynamic mitigation roadmaps based on system risks.", "tools": "AI Plan Generators, Universal Markdown Templates"},
    {"id": "L-10", "title": "AI-Driven Test Case Generation: Functional vs. Non-Functional", "type": "Video + Hands-On", "concepts": "Deterministic output management; mapping textual criteria to strict structured JSON/CSV records.", "impl": "Format multi-variate test script parameters designed for instantaneous injection into core test trackers.", "tools": "TestRail Core API, Jira Zephyr Automation Tools"},
    {"id": "L-11", "title": "Combinatorial Data Generation: Equivalence Partitioning & Boundary Values", "type": "Code-Along", "concepts": "Synthetic asset creation; calculating programmatic ranges for complex database schemas or payment limits.", "impl": "Assemble massive dynamic mock record data suites containing extreme data bounds and edge formatting anomalies.", "tools": "Data Mock Gen Utilities, Custom AI Arrays"},
    {"id": "L-12", "title": "High-Fidelity Bug Reporting & Automated Triage Recommendations", "type": "Video + Template Design", "concepts": "Translating structural system error output and raw failure trace stacks into structured engineering logs.", "impl": "Build a configuration parsing standard error streams to isolate execution failures and pinpoint root-causes.", "tools": "Bug Tracking Systems, Root Cause Analyser Hubs"},
    {"id": "A-02", "title": "Section Assignment: The End-to-End Artifact Challenge", "type": "Hands-On Coding", "concepts": "Executing complete lifecycle artifacts mapping using integrated multi-step AI instructions.", "impl": "Deliverable: Given a live fintech description asset, extract 15 edge cases and build full data schemas.", "tools": "Data Validation Frameworks, Excel Formatting Engines"},

    # SECTION 3
    {"section": "Section 3: Next-Gen Code Generation: Copilots, Coding Standards, & UI Automation"},
    {"id": "L-13", "title": "Configuring Your AI Pair Programmers: GitHub Copilot & Cursor", "type": "Video + Config", "concepts": "Context optimization parameters; indexing workspace codebases; defining layout parameters with system rules.", "impl": "Configure custom workspace engine profiles (.cursorrules) matching precise enterprise clean code goals.", "tools": "GitHub Copilot Engine, Cursor IDE, Workspace Configs"},
    {"id": "L-14", "title": "AI Terminal Workflows with Claude Code & Augment", "type": "Demo + Hands-On", "concepts": "CLI-based code manipulation agent workflows; terminal multi-file refactoring and codebase audit systems.", "impl": "Execute multi-tiered structural additions and codebase corrections from a unified native terminal console.", "tools": "Claude Code Terminal Agent, Augment AI Core CLI"},
    {"id": "L-15", "title": "Generating Selenium WebDriver Frameworks with AI", "type": "Code-Along", "concepts": "Object model encapsulation standards; building abstract interface layers; structural design isolation mapping.", "impl": "Generate multi-class Page Object Models (POM) and modular test files using advanced IDE generation tools.", "tools": "Selenium WebDriver (Java/Python), Page Object Pattern"},
    {"id": "L-16", "title": "Modern Web Automation: Writing Scalable Playwright Scripts", "type": "Code-Along", "concepts": "Asynchronous event handling; utilizing intelligent dynamic selectors; evaluating browser state mechanisms.", "impl": "Generate concurrent integration test layers; run self-correcting locator functions against volatile targets.", "tools": "Playwright, Stagehand Engine, Node.js Engine"},
    {"id": "L-17", "title": "Front-End Testing Speedrun: Cypress Test Generation", "type": "Code-Along", "concepts": "Embedded application interception patterns; creating custom browser control commands via semantic tools.", "impl": "Assemble automated tests targeting custom JS runtime mutations and localized layout frameworks.", "tools": "Cypress Framework, JavaScript/TypeScript"},
    {"id": "L-18", "title": "BDD Excellence: Cucumber Gherkin & Auto-Generated Step Definitions", "type": "Video + Hands-On", "concepts": "Behavioral domain logic definition; systematic regex mapping structures linking human logic to code suites.", "impl": "Generate complex feature definitions and run scripts that auto-produce structural step files.", "tools": "Cucumber JVM, Gherkin Syntax Libraries"},
    {"id": "L-19", "title": "Building Custom Test Utility Classes & Framework Configs", "type": "Code-Along", "concepts": "Decoupling environment environments; formatting global fallback strategies; handling dynamic structural properties.", "impl": "Code robust retry logic utilities, customized multi-layer parsers, and centralized environment files.", "tools": "Config Managers, Custom Retry Utilities"},
    {"id": "L-20", "title": "Code Optimization, Refactoring, and Code Reviews with AI", "type": "Video + Interactive", "concepts": "Static code evaluation models; optimizing runtime parameters; isolating anti-patterns and thread leaks.", "impl": "Input fragile legacy test structures to refactor code to use explicit waiting logic and standard patterns.", "tools": "AI Code Audit Utilities, SonarQube Standard Syncs"},
    {"id": "A-03", "title": "Section Assignment: The Automation Framework Upgrade", "type": "Hands-On Coding", "concepts": "Modernization of technical legacy assets into robust modular structural designs via pair tools.", "impl": "Deliverable: Transform a flat unstructured test script into a strict multi-tiered pattern using custom tools.", "tools": "Cursor IDE, Playwright/Selenium Frameworks"},

    # SECTION 4
    {"section": "Section 4: Advanced Integrations: APIs, Databases, CI/CD, and LLM Validation"},
    {"id": "L-21", "title": "REST Assured & Postman API Automation via AI", "type": "Code-Along", "concepts": "Representational state verification; structural transformation of endpoints into descriptive automation files.", "impl": "Ingest complete raw Swagger OpenAPI JSON models to automatically assemble complete validation test scripts.", "tools": "REST Assured Framework, OpenAPI/Swagger Specifications"},
    {"id": "L-22", "title": "JSON Schemas, POJO Generation, and Payload Transformations", "type": "Code-Along", "concepts": "Data representation translation; runtime verification of type tracking records across downstream layers.", "impl": "Compile complex Plain Old Java Objects (POJOs) and JSON schema models from dynamic unmapped system responses.", "tools": "Jackson Data Bind Libraries, POJO Code Builders"},
    {"id": "L-23", "title": "Data Validation: Generating Complex SQL Queries for DB Testing", "type": "Code-Along", "concepts": "Automated data validation logic; mapping application actions to permanent database persistence layers.", "impl": "Generate complex analytical queries with multi-table JOIN operations and data mutations to test consistency.", "tools": "PostgreSQL, MySQL, Database Connectivity Drivers"},
    {"id": "L-24", "title": "Intelligent CI/CD: Integrating LLMs into Jenkins & GitHub Actions", "type": "Video + Demo", "concepts": "Pipeline log aggregation; utilizing models for error evaluation during active deployment pipelines.", "impl": "Build a workflow capturing execution failures to pass logs to an AI for immediate triage generation.", "tools": "Jenkins Pipelines, GitHub Actions, Cloud Runners"},
    {"id": "L-25", "title": "AI Failure Clustering & Telemetry Triage via ReportPortal", "type": "Video + Setup", "concepts": "Pattern group categorization; using AI clustering methodologies to group identical framework log profiles.", "impl": "Integrate reporting engines to categorize logs across dense test matrix executions.", "tools": "ReportPortal Engine, Log Analytical Tools"},
    {"id": "L-26", "title": "Testing the AI: Accuracy, Safety, and Evaluation Metrics", "type": "Video (Theory)", "concepts": "Nondeterministic verification challenges; measuring hallucination metrics, semantic variance, and output formats.", "impl": "Define explicit structural metrics tracking threshold criteria for LLM generation parameters.", "tools": "LLM Verification Metrics, Evaluation Metrics Guides"},
    {"id": "L-27", "title": "The LLM Testing Stack: DeepEval, PromptFoo, and TruLens", "type": "Code-Along", "concepts": "Unit testing infrastructure for model deployments; asserting toxicity metrics and contextual relevance rules.", "impl": "Write systematic validation tests executing deep evaluation metrics against dynamic generation targets.", "tools": "DeepEval Framework, PromptFoo Engine, TruLens Analytics"},
    {"id": "A-04", "title": "Section Assignment: The Pipeline Guardrail Implementation", "type": "Hands-On Coding", "concepts": "Assembling complete automated check pipelines validating both system backends and model targets.", "impl": "Deliverable: Deploy a testing script asserting data payload rules alongside a DeepEval check workflow.", "tools": "Python Testing Infrastructure, DeepEval Assertions"},

    # SECTION 5
    {"section": "Section 5: AI Agents, n8n, Langflow, MCP & Autonomous QA Capstone Projects"},
    {"id": "L-28", "title": "Introduction to AI Agents: Loops, Tools, Memory, and MCP", "type": "Video (Theory)", "concepts": "Autonomous control infrastructure; ReAct execution loops; connecting AI models to files via Model Context Protocol.", "impl": "Map technical interactions defining how models invoke local execution binaries via standard schemas.", "tools": "Model Context Protocol (MCP) Core Spec"},
    {"id": "L-29", "title": "Visual AI Orchestration with n8n & Langflow", "type": "Code-Along", "concepts": "Node-based computational flow designs; embedding semantic vector stores and runtime session states for QA logs.", "impl": "Deploy visual workflows routing systemic failure telemetry into vector matching systems.", "tools": "n8n Enterprise Engine, Langflow Orchestration App"},
    {"id": "L-30", "title": "Codeless AI Automation Engines: Deep Dive into TestRigor", "type": "Video + Tool Demo", "concepts": "Semantic translation of visual systems; automated self-healing locator calculations based on visual change.", "impl": "Build and run codeless checking scenarios utilizing human-readable testing criteria.", "tools": "TestRigor AI Engine, Cloud Regression Engines"},
    {"id": "C-01", "title": "Capstone Project 1: The Autonomous Jira-to-TestPlan Agent (n8n + RAG)", "type": "Portfolio Project", "concepts": "Event-driven system orchestration; leveraging Vector RAG patterns for context enrichment.", "impl": "Build a live trigger workflow: Detect Jira issues -> Query Pinecone for context -> Output complete system test plans.", "tools": "n8n, Pinecone DB, Jira Integration Hooks, OpenAI API"},
    {"id": "C-02", "title": "Capstone Project 2: Self-Healing Automation Engine via MCP Server", "type": "Portfolio Project", "concepts": "Interactive system feedback; using MCP to patch local files based on runtime console errors.", "impl": "Code an MCP server in TypeScript. If tests fail, the model reads the DOM state, rewrites locators, and retries.", "tools": "Node.js, TypeScript, Playwright Automation, MCP Protocol"},
    {"id": "C-03", "title": "Capstone Project 3: Visual Bug Analyzer SaaS Tool", "type": "Portfolio Project", "concepts": "Multimodal vision analytics; image processing logic; programmatic UI bug generation.", "impl": "Build a pipeline processing failure images through vision models to extract design bugs and file reports.", "tools": "Vision LLM API, Screenshot Interceptors, Bug Trackers"},
    {"id": "L-31", "title": "Course Wrap-Up & Building Your Personal AI QA Career Path", "type": "Video", "concepts": "Strategic technical presentation; establishing AI portfolio footprints; analyzing coming automation vectors.", "impl": "Construct an deployment map outlining personal engineering growth vectors over the upcoming lifecycle phases.", "tools": "GitHub Architecture Repositories, Career Path Maps"}
]

current_row = 2
for entry in syllabus_data:
    if "section" in entry:
        # It's a section header row
        ws_plan.row_dimensions[current_row].height = 26
        ws_plan.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=6)
        cell = ws_plan.cell(row=current_row, column=1, value=entry["section"])
        cell.font = font_section
        cell.fill = fill_accent
        cell.alignment = Alignment(horizontal="left", vertical="center")
        current_row += 1
    else:
        # It's a lecture row
        ws_plan.row_dimensions[current_row].height = 22
        
        # Determine coloring based on assignment or capstone
        is_assignment = entry["id"].startswith("A-") or entry["id"].startswith("C-")
        row_fill = PatternFill(start_color="EAFAF1", end_color="EAFAF1", fill_type="solid") if is_assignment else (fill_zebra if current_row % 2 == 0 else None)
        
        fields = [entry["id"], entry["title"], entry["type"], entry["concepts"], entry["impl"], entry["tools"]]
        
        for col_idx, text in enumerate(fields, 1):
            c = ws_plan.cell(row=current_row, column=col_idx, value=text)
            c.font = font_bold_data if col_idx in [1, 2] else font_body
            if row_fill:
                c.fill = row_fill
            c.border = thin_border
            # Alignments
            if col_idx in [1, 3]:
                c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            else:
                c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                
        current_row += 1

# ----------------- CLEAN UP COLUMN WIDTHS FOR BOTH SHEETS -----------------
# Sheet 1 Autofit Widths
ws_dash.column_dimensions['A'].width = 32
ws_dash.column_dimensions['B'].width = 45
ws_dash.column_dimensions['C'].width = 75

# Sheet 2 Autofit Widths
fixed_widths = [14, 42, 18, 55, 55, 38]
for col_idx, width in enumerate(fixed_widths, 1):
    ws_plan.column_dimensions[get_column_letter(col_idx)].width = width

# Save the polished workbook
filename = "AI_Driven_Automation_QA_Masterclass_Syllabus.xlsx"
wb.save(filename)
print(f"Workbook successfully built and saved as {filename}")