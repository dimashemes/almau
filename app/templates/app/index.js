document.addEventListener('DOMContentLoaded', function() {
    const translations = {
        en: {
            welcome: "Welcome to AlmaU",
            sendap: "Send Application"
        },
        ru: {
            welcome: "Добро пожаловать в AlmaU",
            sendap: "Отправить заявку"
        },
        kz: {
            welcome: "AlmaU қош келдіңіз",
            sendap: "Өтініш жіберу"
        }
    };

    function changeLanguage() {
        const selectedLang = document.getElementById("languageSwitcher").value;
        
        const langData = translations[selectedLang];

        document.getElementById("welcome").textContent = langData.welcome;
        document.getElementById("sendap").textContent = langData.sendap;
    }

    document.getElementById("languageSwitcher").addEventListener('change', changeLanguage);

    changeLanguage();
});
