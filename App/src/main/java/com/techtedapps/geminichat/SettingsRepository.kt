package com.techtedapps.geminichat

import android.content.Context
import android.content.SharedPreferences

class SettingsRepository(context: Context) {
    private val prefs: SharedPreferences = context.getSharedPreferences("gemini_chat_prefs", Context.MODE_PRIVATE)

    fun saveSettings(apiKey: String, modelName: String) {
        with(prefs.edit()) {
            putString("api_key", apiKey)
            putString("model_name", modelName)
            apply()
        }
    }

    fun getApiKey(): String {
        return prefs.getString("api_key", "") ?: ""
    }

    fun getModelName(): String {
        return prefs.getString("model_name", "gemini-2.5-flash") ?: "gemini-2.5-flash"
    }

    fun saveTemperature(temperature: Float) {
        with(prefs.edit()) {
            putFloat("temperature", temperature)
            apply()
        }
    }

    fun getTemperature(): Float {
        return prefs.getFloat("temperature", 0.7f)
    }
}
