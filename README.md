<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FIFA World Cup 2026 Match Prediction System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f3460 0%, #1a5c3a 50%, #0f3460 100%);
            color: #333;
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Navigation Bar */
        nav {
            background: rgba(15, 52, 96, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        nav a:hover {
            background: #00d4ff;
            color: #0f3460;
            transform: translateY(-2px);
        }

        /* Container Principal */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header Hero */
        .hero {
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(26, 92, 58, 0.2) 100%);
            margin: 2rem 0;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            animation: slideDown 0.8s ease;
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero h1 {
            font-size: 3.5rem;
            color: #00d4ff;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        .hero p {
            font-size: 1.2rem;
            color: #fff;
            margin-bottom: 1.5rem;
            font-weight: 300;
        }

        .badges {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin: 2rem 0;
        }

        .badge {
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: #fff;
            padding: 0.6rem 1.2rem;
            border-radius: 25px;
            font-weight: 600;
            font-size: 0.9rem;
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
            transition: all 0.3s ease;
        }

        .badge:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.5);
        }

        .badge.green {
            background: linear-gradient(135deg, #1a5c3a 0%, #2d9f4f 100%);
            box-shadow: 0 4px 15px rgba(45, 159, 79, 0.3);
        }

        .badge.green:hover {
            box-shadow: 0 6px 20px rgba(45, 159, 79, 0.5);
        }

        .badge.orange {
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
        }

        .badge.orange:hover {
            box-shadow: 0 6px 20px rgba(255, 107, 53, 0.5);
        }

        .badge.red {
            background: linear-gradient(135deg, #d62828 0%, #f77f00 100%);
            box-shadow: 0 4px 15px rgba(214, 40, 40, 0.3);
        }

        .badge.red:hover {
            box-shadow: 0 6px 20px rgba(214, 40, 40, 0.5);
        }

        .hero img {
            max-width: 100%;
            height: auto;
            margin-top: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }

        .hero img:hover {
            transform: scale(1.02);
        }

        /* Secciones */
        section {
            background: #fff;
            margin: 2rem auto;
            padding: 3rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            animation: fadeIn 0.8s ease;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        section h2 {
            color: #0f3460;
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            border-bottom: 3px solid #00d4ff;
            padding-bottom: 1rem;
        }

        section h3 {
            color: #1a5c3a;
            font-size: 1.5rem;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }

        section ul {
            list-style: none;
            margin-left: 0;
        }

        section ul li {
            padding: 0.8rem 0;
            padding-left: 2rem;
            position: relative;
            color: #555;
        }

        section ul li:before {
            content: "⚽";
            position: absolute;
            left: 0;
            color: #1a5c3a;
            font-size: 1.2rem;
        }

        /* Tablas */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        table th {
            background: linear-gradient(135deg, #0f3460 0%, #1a5c3a 100%);
            color: #fff;
            padding: 1.2rem;
            text-align: left;
            font-weight: 600;
            font-size: 1rem;
        }

        table td {
            padding: 1rem 1.2rem;
            border-bottom: 1px solid #eee;
            transition: all 0.3s ease;
        }

        table tr:hover {
            background: #f0f8ff;
        }

        table tr:last-child td {
            border-bottom: none;
        }

        /* Código */
        pre {
            background: #1e1e1e;
            color: #00d4ff;
            padding: 1.5rem;
            border-radius: 10px;
            overflow-x: auto;
            margin: 1.5rem 0;
            border-left: 4px solid #00d4ff;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        code {
            font-family: 'Courier New', monospace;
            font-size: 0.95rem;
        }

        /* Diagrama ASCII */
        .diagram {
            background: #f5f5f5;
            padding: 2rem;
            border-radius: 10px;
            font-family: 'Courier New', monospace;
            color: #0f3460;
            text-align: center;
            margin: 2rem 0;
            border-left: 4px solid #1a5c3a;
            overflow-x: auto;
        }

        /* Cajas de característica */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .feature-card {
            background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%);
            padding: 2rem;
            border-radius: 10px;
            border-left: 4px solid #00d4ff;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2);
            border-left-color: #1a5c3a;
        }

        .feature-card h4 {
            color: #0f3460;
            margin-bottom: 0.8rem;
            font-size: 1.1rem;
        }

        .feature-card p {
            color: #666;
            font-size: 0.95rem;
        }

        /* Gallery */
        .gallery {
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            margin: 2rem 0;
        }

        .gallery img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease;
        }

        .gallery img:hover {
            transform: scale(1.05);
        }

        /* Botón CTA */
        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: #fff;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            margin: 1rem 0.5rem;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.5);
        }

        .cta-button.green {
            background: linear-gradient(135deg, #1a5c3a 0%, #2d9f4f 100%);
            box-shadow: 0 4px 15px rgba(45, 159, 79, 0.3);
        }

        .cta-button.green:hover {
            box-shadow: 0 6px 20px rgba(45, 159, 79, 0.5);
        }

        /* Footer */
        footer {
            background: #0f3460;
            color: #fff;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            border-top: 3px solid #00d4ff;
        }

        footer h3 {
            color: #00d4ff;
            margin-bottom: 1rem;
        }

        /* Grid Layout para tablas grandes */
        .portfolio-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin: 2rem 0;
        }

        .portfolio-item {
            background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%);
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            border: 2px solid #00d4ff;
            transition: all 0.3s ease;
        }

        .portfolio-item:hover {
            border-color: #1a5c3a;
            box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2);
        }

        .portfolio-item h4 {
            color: #0f3460;
            margin-bottom: 0.5rem;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.2rem;
            }

            nav ul {
                gap: 0.5rem;
            }

            nav a {
                padding: 0.4rem 0.8rem;
                font-size: 0.9rem;
            }

            section {
                padding: 2rem;
            }

            .features-grid {
                grid-template-columns: 1fr;
            }

            .portfolio-grid {
                grid-template-columns: 1fr;
            }

            table {
                font-size: 0.9rem;
            }

            table td, table th {
                padding: 0.8rem;
            }

            .gallery {
                flex-direction: column;
                align-items: center;
            }
        }

        /* Animación de entrada */
        .fade-in-up {
            animation: fadeInUp 0.8s ease forwards;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="#overview">Overview</a></li>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="#pipeline">Pipeline</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#example">Example</a></li>
            <li><a href="#portfolio">Portfolio</a></li>
        </ul>
    </nav>

    <!-- Hero Section -->
    <div class="hero">
        <div class="container">
            <h1>⚽ FIFA World Cup 2026 Match Prediction System</h1>
            <p>Machine Learning project for predicting FIFA World Cup match outcomes using <strong>XGBoost</strong>, <strong>Elo Ratings</strong>, and <strong>Poisson Goal Modeling</strong></p>
            
            <div class="badges">
                <div class="badge">Python-3.12</div>
                <div class="badge green">XGBoost-ML</div>
                <div class="badge red">Streamlit-Dashboard</div>
                <div class="badge orange">Scikit-Learn-Modeling</div>
            </div>

            <img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python Badge">
            <img src="https://img.shields.io/badge/XGBoost-ML-green" alt="XGBoost Badge">
            <img src="https://img.shields.io/badge/Streamlit-Dashboard-red" alt="Streamlit Badge">
            <img src="https://img.shields.io/badge/Scikit--Learn-Modeling-orange" alt="Scikit-Learn Badge">
        </div>
    </div>

    <!-- Overview Section -->
    <div class="container">
        <section id="overview">
            <h2>🌎 Overview</h2>
            <p>This project is an end-to-end Machine Learning system designed to predict international football matches with a specific focus on FIFA World Cup scenarios.</p>
            
            <p style="margin-top: 1.5rem;"><strong>The pipeline combines:</strong></p>
            
            <ul style="margin-top: 1rem;">
                <li>Elo Rating calculations from historical international matches</li>
                <li>XGBoost Poisson regression models for expected goals prediction</li>
                <li>Poisson probability distributions for scoreline simulation</li>
                <li>Interactive Streamlit dashboard for visualization</li>
            </ul>

            <p style="margin-top: 1.5rem; padding: 1.5rem; background: #f0f8ff; border-left: 4px solid #00d4ff; border-radius: 5px; color: #0f3460;">
                <strong>📊 Dataset:</strong> The model is trained using more than <strong>49,000 historical international matches</strong> and generates realistic tournament-style predictions including score probabilities and match outcome distributions.
            </p>
        </section>

        <!-- Dashboard Section -->
        <section id="dashboard">
            <h2>🏆 Example Dashboard</h2>
            <p>The application provides comprehensive match analysis and predictions:</p>
            
            <div class="features-grid">
                <div class="feature-card">
                    <h4>⚡ Expected Goals (xG)</h4>
                    <p>Predicted scoring output for each team based on historical patterns and current form</p>
                </div>
                <div class="feature-card">
                    <h4>📊 Win / Draw / Loss Probabilities</h4>
                    <p>Complete probability distribution for all possible match outcomes</p>
                </div>
                <div class="feature-card">
                    <h4>🎯 Most Likely Scoreline</h4>
                    <p>The statistically most probable final score based on Poisson modeling</p>
                </div>
                <div class="feature-card">
                    <h4>🏅 Top 10 Predicted Results</h4>
                    <p>Ranked list of the most probable score combinations</p>
                </div>
                <div class="feature-card">
                    <h4>📈 Poisson Goal Matrix</h4>
                    <p>Complete probability distribution for every realistic score combination</p>
                </div>
                <div class="feature-card">
                    <h4>🌡️ Probability Heatmaps</h4>
                    <p>Visual representation of scoring probabilities and match dynamics</p>
                </div>
            </div>
        </section>

        <!-- Pipeline Section -->
        <section id="pipeline">
            <h2>⚙️ Machine Learning Pipeline</h2>
            
            <div class="diagram">
Historical International Matches
                │
                ▼
         Elo Calculation
                │
                ▼
      Feature Engineering
                │
                ▼
     XGBoost Goal Prediction
                │
                ▼
      Expected Goals (λ)
                │
                ▼
       Poisson Simulation
                │
                ▼
 Match Outcome Probabilities
                │
                ▼
      Interactive Dashboard
            </div>
        </section>

        <!-- Features Section -->
        <section id="features">
            <h2>🧠 Model Features</h2>
            
            <div class="portfolio-grid" style="grid-template-columns: 1fr 1fr; gap: 2rem;">
                <div style="background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00d4ff;">
                    <h4 style="color: #0f3460; margin-bottom: 0.5rem;">⚡ Elo Difference</h4>
                    <p style="color: #666;">National team strength differential based on historical performance</p>
                </div>

                <div style="background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00d4ff;">
                    <h4 style="color: #0f3460; margin-bottom: 0.5rem;">🌍 Neutral Venue</h4>
                    <p style="color: #666;">World Cup style neutral-site adjustment</p>
                </div>

                <div style="background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00d4ff;">
                    <h4 style="color: #0f3460; margin-bottom: 0.5rem;">🏆 Official Match Flag</h4>
                    <p style="color: #666;">Distinguishes official competitions from friendly matches</p>
                </div>

                <div style="background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00d4ff;">
                    <h4 style="color: #0f3460; margin-bottom: 0.5rem;">⭐ World Cup Weighting</h4>
                    <p style="color: #666;">Additional importance assigned to FIFA World Cup matches</p>
                </div>

                <div style="background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00d4ff;">
                    <h4 style="color: #0f3460; margin-bottom: 0.5rem;">📈 Expected Goals</h4>
                    <p style="color: #666;">XGBoost-based prediction of team scoring output</p>
                </div>

                <div style="background: linear-gradient(135deg, #f0f8ff 0%, #f0fff4 100%); padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00d4ff;">
                    <h4 style="color: #0f3460; margin-bottom: 0.5rem;">🎯 Poisson Simulation</h4>
                    <p style="color: #666;">Full probability distribution for every realistic scoreline</p>
                </div>
            </div>
        </section>

        <!-- Installation Section -->
        <section id="installation">
            <h2>🚀 Installation & Usage</h2>
            
            <h3>Clone Repository</h3>
            <pre><code>git clone https://github.com/yourusername/worldcup-predictor.git

cd worldcup-predictor

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt</code></pre>

            <h3>Train Models</h3>
            <pre><code>python train_model.py</code></pre>

            <h3>Launch Dashboard</h3>
            <pre><code>streamlit run app.py</code></pre>

            <p style="margin-top: 1.5rem; padding: 1rem; background: #f0f8ff; border-radius: 5px; border-left: 4px solid #00d4ff;">
                Open your browser and navigate to: <code style="background: #fff; padding: 0.3rem 0.6rem; border-radius: 3px; color: #00d4ff;">http://localhost:8501</code>
            </p>
        </section>

        <!-- Example Output Section -->
        <section id="example">
            <h2>🎯 Example Prediction Output</h2>
            
            <div style="background: #1e1e1e; padding: 2rem; border-radius: 10px; color: #00d4ff; font-family: 'Courier New', monospace; margin: 2rem 0; border-left: 4px solid #00d4ff;">
                <div style="margin-bottom: 2rem;">
                    <strong style="color: #fff;">England vs Argentina</strong>
                </div>

                <div style="margin-bottom: 1.5rem;">
                    <div style="color: #fff; margin-bottom: 0.5rem;"><strong>Expected Goals:</strong></div>
                    <div style="margin-left: 1rem;">England     <strong>1.42</strong></div>
                    <div style="margin-left: 1rem;">Argentina   <strong>1.19</strong></div>
                </div>

                <div style="margin-bottom: 1.5rem;">
                    <div style="color: #fff; margin-bottom: 0.5rem;"><strong>Win Probability:</strong></div>
                    <div style="margin-left: 1rem;">England     <strong>41.3%</strong></div>
                    <div style="margin-left: 1rem;">Draw        <strong>27.5%</strong></div>
                    <div style="margin-left: 1rem;">Argentina   <strong>31.2%</strong></div>
                </div>

                <div>
                    <div style="color: #fff; margin-bottom: 0.5rem;"><strong>Most Likely Score:</strong></div>
                    <div style="margin-left: 1rem; font-size: 1.3rem;"><strong>1 - 1</strong></div>
                </div>
            </div>
        </section>

        <!-- Poisson Matrix Section -->
        <section>
            <h2>📉 Poisson Goal Matrix</h2>
            <p>The system generates a complete probability matrix for every realistic score combination, allowing detailed tournament simulations and match outcome analysis.</p>
            
            <div class="gallery">
                <img src="https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1200" alt="Football Analytics">
            </div>
        </section>

        <!-- Portfolio Section -->
        <section id="portfolio">
            <h2>💼 Portfolio Relevance</h2>
            
            <div class="portfolio-grid">
                <div class="portfolio-item">
                    <h4>🤖 Machine Learning Engineering</h4>
                </div>
                <div class="portfolio-item">
                    <h4>📊 Predictive Analytics</h4>
                </div>
                <div class="portfolio-item">
                    <h4>⚽ Sports Analytics</h4>
                </div>
                <div class="portfolio-item">
                    <h4>🧠 Feature Engineering</h4>
                </div>
                <div class="portfolio-item">
                    <h4>📈 Probabilistic Modeling</h4>
                </div>
                <div class="portfolio-item">
                    <h4>🚀 Model Deployment</h4>
                </div>
                <div class="portfolio-item">
                    <h4>🔬 Data Science</h4>
                </div>
                <div class="portfolio-item">
                    <h4>🏗️ End-to-End ML Pipelines</h4>
                </div>
            </div>
        </section>

        <!-- Final Gallery Section -->
        <section style="text-align: center;">
            <div class="gallery">
                <img src="https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=1200" alt="Football Match">
            </div>
            
            <h3 style="margin-top: 2rem; color: #00d4ff;">⚽ Built with Python, XGBoost, Elo Ratings & Poisson Modeling</h3>
            <h2 style="color: #0f3460;">FIFA World Cup 2026 Prediction System</h2>
        </section>
    </div>

    <!-- Footer -->
    <footer>
        <h3>🎯 FIFA World Cup 2026 Match Prediction System</h3>
        <p>An advanced machine learning solution for international football match prediction</p>
        <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.8;">© 2024 - Built with Python, XGBoost, and Machine Learning</p>
    </footer>

    <script>
        // Intersection Observer para animaciones
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-up');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observar todas las secciones
        document.querySelectorAll('section').forEach(section => {
            observer.observe(section);
        });

        // Smooth scroll para navegación
        document.querySelectorAll('nav a').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Efecto hover en badges
        document.querySelectorAll('.badge').forEach(badge => {
            badge.addEventListener('mouseover', function() {
                this.style.transform = 'scale(1.05)';
            });
            badge.addEventListener('mouseout', function() {
                this.style.transform = 'scale(1)';
            });
        });
    </script>
</body>
</html>
