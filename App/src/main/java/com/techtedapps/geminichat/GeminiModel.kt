package com.techtedapps.geminichat

import com.google.genai.client.GenerativeModel
import com.google.genai.common.HarmBlockThreshold
import com.google.genai.common.HarmCategory
import com.google.genai.common.SafetySetting

class GeminiModel(
    apiKey: String,
    modelName: String,
    temperature: Float
) {
    private val permissiveSafetySettings = listOf(
        SafetySetting(HarmCategory.HARASSMENT, HarmBlockThreshold.BLOCK_NONE),
        SafetySetting(HarmCategory.HATE_SPEECH, HarmBlockThreshold.BLOCK_NONE),
        SafetySetting(HarmCategory.SEXUALLY_EXPLICIT, HarmBlockThreshold.BLOCK_NONE),
        SafetySetting(HarmCategory.DANGEROUS_CONTENT, HarmBlockThreshold.BLOCK_NONE),
    )

    val generativeModel: GenerativeModel = GenerativeModel(
        modelName = modelName,
        apiKey = apiKey,
        config = com.google.genai.client.GenerateContentConfig(
            safetySettings = permissiveSafetySettings,
            temperature = temperature
        )
    )
}
