# Chatbot Project

A comprehensive web platform that enables users to configure, create, and deploy customized chatbots for their websites. Visitors can interact with these chatbots and ask questions related to the specific website content.

##  Architecture

This project follows a microservices architecture with three main components:

### Frontend (React + TypeScript)
- **Location**: rontend/
- **Technology**: React with TypeScript and Vite
- **Purpose**: Admin dashboard for chatbot configuration and management
- **Features**: 
  - Bot configuration interface
  - Resource management
  - Design customization
  - Website integration tools

### Backend (Node.js + TypeScript)
- **Location**: ackend/
- **Technology**: Node.js with TypeScript and Express
- **Database**: PostgreSQL with Drizzle ORM
- **Purpose**: Core API and business logic
- **Features**:
  - JWT-based authentication
  - Bot configuration management
  - Database operations
  - AI service communication
  - Static file serving

### AI Service (FastAPI + OpenAI)
- **Location**: servicePython/
- **Technology**: FastAPI with OpenAI API
- **Purpose**: Natural language processing and response generation
- **Features**:
  - RAG (Retrieval-Augmented Generation) implementation
  - Context-aware responses
  - Website-specific knowledge integration

##  Data Flow

```
Frontend (User Input)  Backend (API/DB)  AI Service (NLP)  Backend  Frontend (Response)
```

##  Installation

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- PostgreSQL database
- OpenAI API key

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-project.git
cd chatbot-project
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
npm install

# Copy environment file and configure
cp .env.example .env
# Edit .env with your database credentials and JWT secrets

# Run database migrations
npm run db:migrate

# Seed the database (optional)
npm run db:seed

# Start the backend server
npm run dev
```

The backend will run on http://localhost:3000

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will run on http://localhost:5173

### 4. AI Service Setup

```bash
# Navigate to Python service directory
cd servicePython

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn openai

# Add your OpenAI API key to environment variables
# Create a .env file or set environment variable:
export OPENAI_API_KEY="your-api-key-here"

# Start the FastAPI service
uvicorn service:app --reload --port 8000
```

The AI service will run on http://localhost:8000

##  Configuration

### Environment Variables

#### Backend (.env)
```env
# Database
DATABASE_URL="postgresql://username:password@localhost:5432/chatbot_db"

# JWT
JWT_SECRET="your-jwt-secret"
JWT_REFRESH_SECRET="your-refresh-secret"

# Server
PORT=3000
NODE_ENV=development
```

#### AI Service
```env
OPENAI_API_KEY="your-openai-api-key"
```

##  Usage

1. **Start all services** in the following order:
   - PostgreSQL database
   - Backend server (
pm run dev in ackend/)
   - AI service (uvicorn service:app --reload in servicePython/)
   - Frontend (
pm run dev in rontend/)

2. **Access the application**:
   - Frontend Dashboard: http://localhost:5173
   - Backend API: http://localhost:3000
   - AI Service: http://localhost:8000

3. **Create and configure your chatbot** through the frontend dashboard

4. **Integrate the chatbot** into your website using the generated embed code

##  Testing

A test environment is available in the 	est/ directory for bot integration testing.

```bash
cd test
npm install
npm start
```

##  Project Structure

```
 backend/          # Node.js API server
 frontend/         # React dashboard
 servicePython/    # FastAPI AI service
 test/            # Integration testing
 .github/         # GitHub configuration
```

##  Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Copyright (c) 2025 Chatbot Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

##  Known Issues

- Frontend and AI service components are currently under development
- Some features may be incomplete or in beta

##  Support

For support, please open an issue on GitHub or contact the development team.

---

**Note**: This project is actively being developed. The frontend and Python service components are currently incomplete but under active development.
