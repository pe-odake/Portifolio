# Personal Portfolio

## Overview

A personal portfolio web application built with Django to showcase projects, skills, courses, and certificates. The application features a public-facing portfolio site and a custom admin panel for content management. It serves as a digital showcase for a Systems Development student, highlighting Full-Stack development proficiency with emphasis on Python and Django.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture

**Framework**: Django (Python web framework)
- Standard Django project structure with `core` as the main configuration module
- Single app architecture with `portfolio` handling all portfolio-related functionality
- Class-based views for all pages (TemplateView, ListView, CreateView, UpdateView, DeleteView)
- Django's built-in authentication system for admin panel access

**Data Models**:
- `Perfil` - Profile/About information (name, title, bio, social links, CV link)
- `Projeto` - Projects with Many-to-Many relationship to Skills via `skills` field
- `ProjetoImagem` - Gallery images per project (ForeignKey to Projeto) with `ordem` for ordering
- `Skill` - Reusable skills/tags with icon support (SVG/PNG), with image validators
- `Curso` - Courses/Education
- `Certificado` - Certificates with PDF support
- `Contato` - Contact form submissions

**Key Design Decisions**:
- Custom admin panel instead of Django's default admin (located at `/painel/`)
- Image validation for size (max 5MB) and file extensions via `validate_image_size` validator
- Many-to-Many relationship between Projects and Skills for flexible tagging
- Ordered gallery images per project with carousel support
- Custom `MultipleFileField` form field for multiple image uploads
- Responsive image carousels with touch/swipe support for mobile devices

### Frontend Architecture

**Public Site**:
- Template-based rendering with Django templates
- Bootstrap 5 for responsive layout and components
- Font Awesome for icons
- Custom CSS with CSS variables for theming (dark/light mode toggle)
- JavaScript for interactivity (carousels, theme switching, smooth scrolling)

**Admin Panel**:
- Custom dashboard interface separate from Django admin
- Login required for all admin views
- CRUD operations for all content types
- Multiple file upload support for project galleries

### Static Files

- WhiteNoise middleware for serving static files in production
- Separate static directories: `portfolio/static/` (source) and `staticfiles/` (collected)
- CSS organized by concern: `style.css` (public), `admin.css` (admin panel)

### Database

- SQLite by default (Django's default database)
- Migrations track schema changes
- File-based media storage for images and documents

## External Dependencies

### Python Packages (requirements.txt)
- **Django** - Web framework
- **Gunicorn** - WSGI HTTP server for production deployment
- **Pillow** - Image processing library for ImageField support
- **WhiteNoise** - Static file serving for production

### Frontend CDN Dependencies
- Bootstrap 5.3.2 (CSS and JS)
- Font Awesome 6.4.2 (icons)
- Google Fonts (Inter font family)

### Environment Variables
- `SECRET_KEY` - Django secret key (defaults to insecure dev key)
- `DEBUG` - Debug mode toggle (defaults to True)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts (defaults to *)