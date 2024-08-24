@app.route('/result', methods=['POST'])
def result():
    product_list = request.form['product_list']
    product_list = [product_name.strip() for product_name in product_list.split(',')]
    
    collected_data = []
    for product_name in product_list:
        amazon_prices = search_amazon(product_name)
        walmart_prices = search_walmart(product_name)
        
        collected_data.append({
            "Product Name": product_name,
            "Amazon Prices": amazon_prices,
            "Walmart Prices": walmart_prices
        })
    
    df = pd.DataFrame(collected_data)
    
    # Create a linear regression model
    X = df[['Amazon Prices']]
    y = df['Walmart Prices']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    # Compare predicted prices with actual prices
    comparison_data = []
    for i in range(len(y_test)):
        if y_pred[i] > y_test.values[i]:
            price_change = "Increased"
        elif y_pred[i] < y_test.values[i]:
            price_change = "Decreased"
        else:
            price_change = "No Change"
        
        comparison_data.append({
            "Product Name": df.iloc[X_test.index[i]]['Product Name'],
            "Actual Price": y_test.values[i],
            "Predicted Price": y_pred[i],
            "Price Change": price_change
        })
    
    # Return the comparison data as a JSON response
    return jsonify(comparison_data)
