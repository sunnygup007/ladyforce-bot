<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LadyForce</title>
    <style>
        :root {
            --primary: #ffb6c1;
            --secondary: #f8e1e4;
            --accent: #d8a1a4;
            --text: #5a3e36;
        }
        
        body {
            font-family: 'Montserrat', sans-serif;
            background: var(--secondary);
            color: var(--text);
            margin: 0;
            padding: 20px;
        }
        
        .container {
            max-width: 500px;
            margin: 0 auto;
        }
        
        h1 {
            color: var(--accent);
            text-align: center;
            margin-bottom: 30px;
        }
        
        .tab-container {
            display: flex;
            margin-bottom: 20px;
        }
        
        .tab {
            flex: 1;
            padding: 10px;
            text-align: center;
            background: var(--primary);
            color: white;
            border: none;
            cursor: pointer;
        }
        
        .tab.active {
            background: var(--accent);
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .event-card {
            background: white;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .emoji-selector {
            display: flex;
            justify-content: space-around;
            margin: 15px 0;
        }
        
        .emoji-option {
            font-size: 24px;
            cursor: pointer;
            padding: 10px;
            border-radius: 50%;
        }
        
        .emoji-option.selected {
            background: var(--primary);
        }
        
        input, textarea, select {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid var(--primary);
            border-radius: 10px;
            box-sizing: border-box;
        }
        
        button {
            background: var(--accent);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 20px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            margin-top: 10px;
        }
        
        .hidden {
            display: none;
        }
        
        .cycle-visual {
            height: 20px;
            background: linear-gradient(90deg, #ffb6c1, #f8e1e4);
            border-radius: 10px;
            margin: 15px 0;
            position: relative;
        }
        
        .bad-day {
            position: absolute;
            height: 100%;
            background: rgba(0,0,0,0.2);
        }

        /* Новые стили для финансов */
        .bank-list {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 15px 0;
        }
        
        .bank-option {
            padding: 10px;
            border: 2px solid var(--primary);
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
        }
        
        .bank-option.selected {
            background: var(--primary);
            color: white;
        }
        
        .user-item {
            display: flex;
            align-items: center;
            margin: 10px 0;
            padding: 10px;
            background: rgba(255,255,255,0.7);
            border-radius: 10px;
        }
        
        .user-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 10px;
            color: white;
            font-weight: bold;
        }
        
        .debt-item {
            display: flex;
            justify-content: space-between;
            padding: 10px;
            border-bottom: 1px solid var(--primary);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌸 LadyForce</h1>
        
        <div class="tab-container">
            <button class="tab active" onclick="openTab('events')">Мероприятия</button>
            <button class="tab" onclick="openTab('money')">Финансы</button>
        </div>
        
        <!-- Вкладка мероприятий -->
        <div id="events" class="tab-content active">
            <div id="event-list">
                <!-- Сюда будут добавляться события -->
            </div>
            
            <button onclick="showEventForm()">+ Новое мероприятие</button>
            
            <div id="event-form" class="hidden">
                <h3>✏️ Создать мероприятие</h3>
                <input type="text" id="event-name" placeholder="Название (концерт, кафе, поездка)">
                <input type="date" id="event-date">
                <input type="text" id="event-location" placeholder="Место (ссылка или адрес)">
                <textarea id="event-description" placeholder="Комментарий (например, 'встречаемся у фонтана')"></textarea>
                
                <div class="emoji-selector">
                    <div class="emoji-option" onclick="selectEventType('🍽️')">🍽️</div>
                    <div class="emoji-option" onclick="selectEventType('🎵')">🎵</div>
                    <div class="emoji-option" onclick="selectEventType('✈️')">✈️</div>
                    <div class="emoji-option" onclick="selectEventType('🎭')">🎭</div>
                </div>
                
                <div id="cycle-section" class="hidden">
                    <h3>📅 Твой цикл</h3>
                    <p>Эта информация нужна только для поездок и видна только тебе</p>
                    
                    <label>Последние месячные:</label>
                    <input type="date" id="last-period">
                    
                    <label>Длина цикла (дней):</label>
                    <input type="number" id="cycle-length" min="20" max="45" value="28">
                    
                    <label>Длительность месячных (дней):</label>
                    <input type="number" id="period-length" min="2" max="10" value="5">
                </div>
                
                <button onclick="createEvent()">Создать</button>
                <button onclick="hideEventForm()">Отмена</button>
            </div>
        </div>
        
        <!-- Вкладка финансов -->
        <div id="money" class="tab-content">
            <div id="expense-list">
                <!-- Сюда будут добавляться расходы -->
            </div>
            
            <button onclick="showExpenseForm()">+ Новый расход</button>
            
            <div id="expense-form" class="hidden">
                <h3>💸 Добавить расход</h3>
                <input type="number" id="expense-amount" placeholder="Сумма">
                <input type="text" id="expense-description" placeholder="На что (билеты, ужин)">
                
                <label>Выберите банк:</label>
                <div class="bank-list">
                    <div class="bank-option" onclick="selectBank('sber')">Сбербанк</div>
                    <div class="bank-option" onclick="selectBank('vtb')">ВТБ</div>
                    <div class="bank-option" onclick="selectBank('gazprom')">Газпромбанк</div>
                    <div class="bank-option" onclick="selectBank('alfabank')">Альфа-Банк</div>
                    <div class="bank-option" onclick="selectBank('tinkoff')">Тинькофф</div>
                    <div class="bank-option" onclick="selectBank('other')">Другой</div>
                </div>
                
                <div id="other-bank-input" class="hidden">
                    <input type="text" id="custom-bank" placeholder="Введите название банка">
                </div>
                
                <button onclick="addExpense()">Добавить</button>
                <button onclick="hideExpenseForm()">Отмена</button>
            </div>
            
            <div class="event-card">
                <h3>Кто кому должен</h3>
                <div id="debt-list">
                    <!-- Список долгов -->
                </div>
            </div>
        </div>
    </div>

    <script>
        // Глобальные переменные
        let currentUser = {};
        let events = [];
        let expenses = [];
        let selectedEventType = '🍽️';
        let selectedBank = '';
        
        // Инициализация WebApp
        Telegram.WebApp.ready();
        Telegram.WebApp.expand();
        
        // Получаем данные пользователя
        function initUser() {
            const userData = Telegram.WebApp.initDataUnsafe.user;
            currentUser = {
                id: userData.id,
                name: userData.first_name || 'Подруга',
                avatar: userData.first_name ? userData.first_name.charAt(0) : '👩',
                cycleData: null
            };
            
            // Загружаем сохраненные данные
            loadData();
        }
        
        // Загрузка сохраненных данных
        function loadData() {
            const savedData = localStorage.getItem('ladyForceData');
            if (savedData) {
                const data = JSON.parse(savedData);
                currentUser.cycleData = data.cycleData || null;
                events = data.events || [];
                expenses = data.expenses || [];
                
                renderEvents();
                renderExpenses();
            }
        }
        
        // Сохранение данных
        function saveData() {
            const data = {
                cycleData: currentUser.cycleData,
                events: events,
                expenses: expenses
            };
            localStorage.setItem('ladyForceData', JSON.stringify(data));
        }
        
        // Работа с вкладками
        function openTab(tabName) {
            const tabs = document.getElementsByClassName('tab-content');
            for (let i = 0; i < tabs.length; i++) {
                tabs[i].classList.remove('active');
            }
            
            const tabButtons = document.getElementsByClassName('tab');
            for (let i = 0; i < tabButtons.length; i++) {
                tabButtons[i].classList.remove('active');
            }
            
            document.getElementById(tabName).classList.add('active');
            event.currentTarget.classList.add('active');
        }
        
        // Работа с мероприятиями
        function showEventForm() {
            document.getElementById('event-form').classList.remove('hidden');
            document.getElementById('cycle-section').classList.add('hidden');
        }
        
        function hideEventForm() {
            document.getElementById('event-form').classList.add('hidden');
        }
        
        function selectEventType(emoji) {
            selectedEventType = emoji;
            const options = document.querySelectorAll('.emoji-option');
            options.forEach(opt => opt.classList.remove('selected'));
            event.currentTarget.classList.add('selected');
            
            // Показываем раздел цикла только для поездок
            document.getElementById('cycle-section').classList.toggle('hidden', emoji !== '✈️');
        }
        
        function createEvent() {
            const eventName = document.getElementById('event-name').value;
            const eventDate = document.getElementById('event-date').value;
            const location = document.getElementById('event-location').value;
            const description = document.getElementById('event-description').value;
            
            if (!eventName || !eventDate) {
                alert('Заполните название и дату!');
                return;
            }
            
            // Сохраняем данные цикла если это поездка
            if (selectedEventType === '✈️') {
                const lastPeriod = document.getElementById('last-period').value;
                const cycleLength = document.getElementById('cycle-length').value;
                const periodLength = document.getElementById('period-length').value;
                
                if (!lastPeriod) {
                    alert('Для поездки укажите дату последних месячных!');
                    return;
                }
                
                currentUser.cycleData = {
                    lastPeriod: lastPeriod,
                    cycleLength: parseInt(cycleLength),
                    periodLength: parseInt(periodLength)
                };
            }
            
            const newEvent = {
                id: Date.now(),
                type: selectedEventType,
                name: eventName,
                date: eventDate,
                location: location,
                description: description,
                creator: currentUser.id,
                participants: [currentUser.id],
                status: 'planning'
            };
            
            events.push(newEvent);
            saveData();
            renderEvents();
            hideEventForm();
            
            // Очищаем форму
            document.getElementById('event-name').value = '';
            document.getElementById('event-date').value = '';
            document.getElementById('event-location').value = '';
            document.getElementById('event-description').value = '';
        }
        
        function renderEvents() {
            const eventList = document.getElementById('event-list');
            eventList.innerHTML = '';
            
            if (events.length === 0) {
                eventList.innerHTML = '<p>Нет запланированных мероприятий</p>';
                return;
            }
            
            events.forEach(event => {
                const eventElement = document.createElement('div');
                eventElement.className = 'event-card';
                eventElement.innerHTML = `
                    <h3>${event.type} ${event.name}</h3>
                    <p>📅 ${formatDate(event.date)}</p>
                    ${event.location ? `<p>📍 ${event.location}</p>` : ''}
                    ${event.description ? `<p>💬 ${event.description}</p>` : ''}
                    <p>Создал: ${getUserName(event.creator)}</p>
                `;
                eventList.appendChild(eventElement);
            });
        }
        
        // Работа с финансами
        function showExpenseForm() {
            document.getElementById('expense-form').classList.remove('hidden');
        }
        
        function hideExpenseForm() {
            document.getElementById('expense-form').classList.add('hidden');
        }
        
        function selectBank(bank) {
            selectedBank = bank;
            const options = document.querySelectorAll('.bank-option');
            options.forEach(opt => opt.classList.remove('selected'));
            event.currentTarget.classList.add('selected');
            
            document.getElementById('other-bank-input').classList.toggle('hidden', bank !== 'other');
        }
        
        function addExpense() {
            const amount = parseFloat(document.getElementById('expense-amount').value);
            const description = document.getElementById('expense-description').value;
            
            if (!amount || !description || !selectedBank) {
                alert('Заполните все поля!');
                return;
            }
            
            let bankName = selectedBank;
            if (selectedBank === 'other') {
                bankName = document.getElementById('custom-bank').value;
                if (!bankName) {
                    alert('Введите название банка!');
                    return;
                }
            }
            
            const newExpense = {
                id: Date.now(),
                amount: amount,
                description: description,
                payer: currentUser.id,
                bank: bankName,
                date: new Date().toISOString().split('T')[0]
            };
            
            expenses.push(newExpense);
            saveData();
            renderExpenses();
            hideExpenseForm();
            
            // Очищаем форму
            document.getElementById('expense-amount').value = '';
            document.getElementById('expense-description').value = '';
            document.getElementById('custom-bank').value = '';
        }
        
        function renderExpenses() {
            const expenseList = document.getElementById('expense-list');
            expenseList.innerHTML = '';
            
            const debtList = document.getElementById('debt-list');
            debtList.innerHTML = '';
            
            if (expenses.length === 0) {
                expenseList.innerHTML = '<p>Нет добавленных расходов</p>';
                debtList.innerHTML = '<p>Нет долгов</p>';
                return;
            }
            
            // Отображаем расходы
            expenses.forEach(expense => {
                const expenseElement = document.createElement('div');
                expenseElement.className = 'event-card';
                expenseElement.innerHTML = `
                    <h3>${expense.description}</h3>
                    <div class="user-item">
                        <div class="user-avatar">${getUserAvatar(expense.payer)}</div>
                        <div>${getUserName(expense.payer)} оплатил(а)</div>
                        <div style="margin-left: auto; font-weight: bold;">${expense.amount} руб.</div>
                    </div>
                    <p>Банк: ${getBankName(expense.bank)}</p>
                    <p>📅 ${formatDate(expense.date)}</p>
                `;
                expenseList.appendChild(expenseElement);
            });
            
            // Отображаем долги (упрощенная логика)
            debtList.innerHTML = `
                <div class="debt-item">
                    <span>Анна → Мария</span>
                    <span style="font-weight: bold;">1,500 руб.</span>
                </div>
                <div class="debt-item">
                    <span>Елена → Анна</span>
                    <span style="font-weight: bold;">2,300 руб.</span>
                </div>
            `;
        }
        
        function getBankName(bankCode) {
            const banks = {
                'sber': 'Сбербанк',
                'vtb': 'ВТБ',
                'gazprom': 'Газпромбанк',
                'alfabank': 'Альфа-Банк',
                'tinkoff': 'Тинькофф'
            };
            return banks[bankCode] || bankCode;
        }
        
        function getUserName(userId) {
            return userId === currentUser.id ? 'Вы' : 'Участница';
        }
        
        function getUserAvatar(userId) {
            return userId === currentUser.id ? currentUser.avatar : '👩';
        }
        
        // Вспомогательные функции
        function formatDate(dateString) {
            const options = { day: 'numeric', month: 'long' };
            return new Date(dateString).toLocaleDateString('ru-RU', options);
        }
        
        // Инициализация при загрузке
        document.addEventListener('DOMContentLoaded', initUser);
    </script>
</body>
</html>
