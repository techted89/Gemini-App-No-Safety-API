// Root build.gradle.kts (Project level)

plugins {
    // ACTION: Updated AGP to the recommended 8.13.0 for better compatibility
    // with Kotlin 2.0.0 and modern SDK versions (like compileSdk 36).
    id("com.android.application") version "8.13.0" apply false
    id("com.android.library") version "8.13.0" apply false
    
    // Updated Kotlin to 2.0.0 for stability (first stable 2.x version).
    // The Compose compiler plugin is now handled implicitly by the Android Gradle Plugin (AGP 8.13.0)
    // based on this Kotlin version.
    id("org.jetbrains.kotlin.android") version "2.0.0" apply false 
}