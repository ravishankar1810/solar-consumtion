# 🌞 Energy Consumption Analysis & Solar Panel Savings Estimator

This project analyzes hourly energy consumption patterns and simulates solar energy production using PVLib to estimate cost savings based on different solar panel configurations.

It is designed to help individuals or organizations evaluate the impact of installing solar panels based on their energy usage.

---

## 📌 Features

- 📊 Polynomial regression to model energy usage ("Duck Curve")
- 🕒 Hourly energy load profile generation
- ☀️ Solar power simulation using PVLib based on real location and panel data
- 💶 Savings calculation for different solar panel setups
- 📁 Export results to CSV and image files

---

## 📂 Folder Structure

.
├── Energy Consumption.py
├── hourly energy consumption.py
├── solar panel energy production and calculating the potential savings for different numbers of panels.py
├── solar_modules.py
├── sazonal_consumption.py
├── prices_aux.py
├── AC_helper.py
├── CONSUMPTION_FUNC.py
├── Consumption.txt
├── Final_Calcs/
└── polynomial_regression_degree_*.png


---

## 📊 Technologies Used

- **Python 3**
- **Pandas** – Data manipulation
- **NumPy** – Numeric computations
- **Matplotlib / Seaborn** – Visualization
- **PVLib** – Solar energy modeling
- **CSV** – Data input/output

---

## 🚀 How to Run

### 1. Install Required Packages

```bash
pip install pandas numpy matplotlib pvlib seaborn
```

### 2. Prepare Input Files

Ensure the following files are available:

Consumption.txt – Hourly energy data

sazonal_consumption.py, prices_aux.py, AC_helper.py, CONSUMPTION_FUNC.py – Helper modules with data and configuration

### 3. Run Analysis Scripts

- Generate polynomial regression plots:

python "Energy Consumption.py"

- Estimate solar savings:

python "solar panel energy production and calculating the potential savings for different numbers of panels.py"

### 📁 Output

- PNG graphs showing energy consumption regression (Duck Curve)

- CSV files showing:

   - Solar panel specs

   - Yearly energy output

   - Cost savings

   - Recommended number of panels

# Example:

Final_Calcs/Porto/100euro__panels_0.csv

### 📈 Example Use Case

A student living in Porto wants to analyze their energy bill and see:

 - How they consume electricity hour by hour

 - Which solar panels would save them the most money

 - How many panels they should install

This tool gives them an answer based on consumption history and real solar models.

### 🛠️ To-Do / Future Enhancements

- Add graphical user interface (GUI)

- Add weather API integration

- Support for multiple geographic regions

- Export interactive charts using Plotly or Dash

### 📄 License

This project is licensed under the MIT License.

### 🙋‍♂️ Author

## Ravi Shankar Kumar Singh

Connect with me on LinkedIn: https://www.linkedin.com/in/ravi-shankar-singh-08361b290/
Check out more on GitHub: https://github.com/ravishankar1810

### 🤝 Contributions

Feel free to fork the project, open issues, or submit pull requests if you'd like to contribute or improve this tool.



---

Let me know if you'd like this as a downloadable `.md` file or want to personalize the author section further (like Link
