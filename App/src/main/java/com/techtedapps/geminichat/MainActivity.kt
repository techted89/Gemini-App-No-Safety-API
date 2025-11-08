package com.techtedapps.geminichat

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.techtedapps.geminichat.ui.ChatScreen
import com.techtedapps.geminichat.ui.SettingsScreen
import com.techtedapps.geminichat.ui.theme.GeminiChatTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val settingsRepository = SettingsRepository(this)
        val viewModel: ChatViewModel by viewModels { ChatViewModelFactory(settingsRepository) }
        setContent {
            GeminiChatTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    val navController = rememberNavController()
                    NavHost(navController = navController, startDestination = "chat") {
                        composable("chat") {
                            ChatScreen(
                                viewModel = viewModel,
                                onNavigateToSettings = { navController.navigate("settings") }
                            )
                        }
                        composable("settings") {
                            SettingsScreen(
                                onSave = { apiKey, modelName, temperature ->
                                    settingsRepository.saveSettings(apiKey, modelName)
                                    settingsRepository.saveTemperature(temperature)
                                    navController.popBackStack()
                                },
                                apiKey = settingsRepository.getApiKey(),
                                modelName = settingsRepository.getModelName(),
                                temperature = settingsRepository.getTemperature()
                            )
                        }
                    }
                }
            }
        }
    }
}
