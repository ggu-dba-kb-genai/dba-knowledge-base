---
type: Session
resource: https://www.youtube.com/watch?v=KHqndz5ElF0
title: 'Session 12: Practical RPA — Hands-on with Power Apps & UiPath'
description: A hands-on laboratory session demonstrating practical robotic process
  automation (RPA) workflows using Microsoft Power Apps and UiPath SMTP integration.
tags:
- Robotic Process Automation
- RPA
- Microsoft Power Apps
- UiPath
- SMTP Configuration
- Integration
- Hands-on Lab
timestamp: '2025-08-30'
---

Following an introduction to Robotic Process Automation (RPA) in the prior lecture, this laboratory session transitions students into practical development of low-code tools and automated workflows. The session begins with a review of the automation journey, contrasting basic automation (simple scripting, macros, and Remote Desktop Automation / RDA) with intermediate RPA (using chatbots and structured tasks) and Intelligent Process Automation (IPA), which integrates OCR, natural language processing, and cognitive machine learning. The instructor clarifies these tiers with real-world examples: basic automation is represented by auto-formatting Excel reports, intermediate automation by chatbots handling structured HR queries, and intelligent automation by scanning bills and parsing unstructured data.

The first practical demonstration guides students through the step-by-step process of creating a blank canvas application in Microsoft Power Apps using a tablet layout. Students connect the application to an external Google Sheet database that holds a mid-semester course schedule. Upon establishing this connection, Power Apps appends a unique `powerapps-id` column (Column H) to the Google Sheet. Students design the user interface by inserting a vertical gallery to display entries and adding an edit form. A crucial technical detail is data binding: students learn to map the edit form's `Item` property to `gallery.selected` (specifically referring to local gallery instances like `gallery1` or `gallery2`) rather than binding the raw data source. Lastly, they add a button, rename it to "Save Changes", and program its `OnSelect` action with the `SubmitForm(formName)` method to push changes back to Google Sheets. Students experience live testing, noting that although the database updates successfully, there is a minor latency that requires a manual refresh of the data source within the app to reflect external changes.

The second half of the lab introduces students to developing a basic RPA workflow to automate communication using UiPath Studio (covering both desktop and web versions). Students create a blank project under the "RPA Workflow" process template and deploy the `Send SMTP Email` activity. They configure SMTP server settings, including setting the mail server to `smtp.gmail.com`, configuring the secure port to `587`, and keeping the secure connection setting on `auto`. A key security requirement highlighted is generating and using a Google App Password instead of a primary Gmail password for API-driven authentication. Inside UiPath, students write standard string parameters within double quotes and practice concatenating string constants with variables using the `+` operator (e.g., `"Hello " + nameVar`). The session concludes by discussing how to scale this basic activity to enterprise-level batch mailing by feeding the SMTP activity from an uploaded Excel file containing recipient lists, custom subjects, and body parameters.

# Key Concepts

- **[Robotic Process Automation & Intelligent Process Automation](../concepts/agentic-ai-autonomous-systems.md)** — RPA ranges from basic automated macros and scripting to cognitive and decision-support systems in IPA. The session reviews the automation spectrum from basic (RDA) to intelligent stages (IPA), demonstrating how workflows connect structured interfaces to complex operations.
- **[AI Security and Robustness](../concepts/ai-security-robustness.md)** — Integrating third-party automation tools requires secure credential management. The session details how to configure SMTP pipelines securely by generating and utilizing Google App Passwords rather than primary login credentials to prevent credential exposure.
- **Blank Canvas App Design** — Building user interfaces in Microsoft Power Apps with a tablet layout, utilizing components such as Vertical Galleries to read and display data and Edit Forms to modify records.
- **Data Binding and Form Management** — Explicitly binding form fields to a selected gallery item using the `gallery.selected` syntax under the form's `Item` property to enable item-by-item editing and avoid rendering errors.
- **Action Triggers and OnSelect Events** — Writing low-code formulas (specifically `SubmitForm(FormName)`) in a button's `OnSelect` action block to trigger backend database writes.
- **SMTP Mail Automation** — Configuring the `Send SMTP Email` activity in UiPath to connect via `smtp.gmail.com` on port `587` to automate communications.
- **Variable Concatenation in Low-Code/No-Code** — Declaring variables in the Data Manager, wrapping string literals in double quotes, and concatenating strings with variables using the `+` operator.

# Topics Covered

- Recap of RDA, RPA, and IPA characteristics (complexity, cognitive capabilities, and decision support)
- Microsoft Power Apps account registration and navigation
- Building a Blank Canvas App with Tablet Layout
- Connecting Google Sheets as a low-code database source
- Implementing a Vertical Gallery and binding it to Google Sheet columns
- Inserting and customizing an Edit Form
- Resolving form binding issues by configuring the `Item` property to `gallery.selected` (specifically mapping matching gallery instances)
- Programming button actions via the `OnSelect` property using `SubmitForm`
- Testing database updates and handling synchronization latency in Power Apps
- Setting up UiPath Studio (desktop and web versions) and cloud registration
- Creating a blank RPA Workflow project
- Integrating the `Send SMTP Email` activity and managing library packages
- Generating and configuring a Google App Password for secure third-party authentication
- Setting up SMTP credentials (`smtp.gmail.com`, Port `587`, Secure Connection: Auto)
- Declaring and concatenating variables in UiPath using double quotes and the `+` operator
- Discussion on scaling SMTP activities with Excel spreadsheets for customized mass mailing

# Materials

- **Chat**: Yes, chat is present.
- **Slides**: None available.
- **Recording**: [YouTube Video KHqndz5ElF0](https://www.youtube.com/watch?v=KHqndz5ElF0)

# Related

- Part of [Emerging Digital Technologies](../courses/c1-emerging-digital-technologies.md)
- Sibling Sessions:
  - Previous: [Session 11](c1-emerging-digital-technologies-session-11.md)
  - Next: [Session 13](c1-emerging-digital-technologies-session-13.md)

# Citations

1. `https://www.youtube.com/watch?v=KHqndz5ElF0` — Session 12 Video Recording.
2. Microsoft Power Apps documentation on Canvas apps and vertical galleries: `https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/`
3. UiPath Studio documentation on Send SMTP Email Activity: `https://docs.uipath.com/activities/other/latest/developer/send-smtp-email`
