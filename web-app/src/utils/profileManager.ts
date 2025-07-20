import type { ProfileData, FormData, ValidationResult, BasicInfo, AdvancedSettings, AdditionalInfo, Metadata } from '../types';

// Validation function for basic info
export function validateBasicInfo(purpose: string, attire: string, background: string, vibe: string): ValidationResult {
  if (!purpose) {
    return { isValid: false, message: "⚠️ Please select a purpose for your portrait" };
  }
  if (!attire) {
    return { isValid: false, message: "⚠️ Please select your preferred attire" };
  }
  if (!background) {
    return { isValid: false, message: "⚠️ Please select a background style" };
  }
  if (!vibe) {
    return { isValid: false, message: "⚠️ Please select your desired vibe" };
  }
  return { isValid: true, message: "✅ All inputs valid" };
}

// Create profile data from form data
export function createProfileData(formData: FormData): ProfileData {
  const basicInfo: BasicInfo = {
    purpose: formData.purpose,
    attire: formData.attire,
    background: formData.background,
    vibe: formData.vibe,
  };

  const advancedSettings: AdvancedSettings = {
    lighting: formData.lighting,
    mood: formData.mood,
    age_range: formData.age_range,
    gender: formData.gender,
    ethnicity: formData.ethnicity,
    resolution: formData.resolution,
  };

  const additionalInfo: AdditionalInfo = {
    reference_photo: formData.reference_photo?.name || null,
    custom_notes: formData.custom_notes || null,
    preset_used: formData.preset_name || null,
  };

  const metadata: Metadata = {
    timestamp: new Date().toLocaleString(),
    version: "2.0",
    created_by: "APEX Portrait Generator (Web)",
  };

  return {
    basic_info: basicInfo,
    advanced_settings: advancedSettings,
    additional_info: additionalInfo,
    metadata,
  };
}

// Generate advanced prompt from form data
export function generateAdvancedPrompt(formData: FormData): string {
  const { purpose, attire, background, vibe, lighting, mood, custom_notes } = formData;
  
  const promptParts = [
    `Professional portrait for ${purpose.toLowerCase()}`,
    `wearing ${attire.toLowerCase()}`,
    `with ${background.toLowerCase()} background`,
    `conveying a ${vibe.toLowerCase()} vibe`,
    `using ${lighting.toLowerCase()}`,
    `with ${mood.toLowerCase()} mood`,
  ];

  let prompt = promptParts.join(', ');
  
  if (custom_notes) {
    prompt += `. Additional details: ${custom_notes}`;
  }

  // Add technical specifications
  prompt += '. High-quality, professional photography, sharp focus, natural skin texture, proper lighting, photorealistic.';

  return prompt;
}

// Save profile to localStorage
export function saveProfileToStorage(profile: ProfileData, filename?: string): string {
  const savedProfiles = getStoredProfiles();
  const profileName = filename || `portrait_profile_${new Date().toISOString().replace(/[:.]/g, '-')}`;
  
  savedProfiles[profileName] = profile;
  localStorage.setItem('apex_profiles', JSON.stringify(savedProfiles));
  
  return profileName;
}

// Get all stored profiles
export function getStoredProfiles(): Record<string, ProfileData> {
  try {
    const stored = localStorage.getItem('apex_profiles');
    return stored ? JSON.parse(stored) : {};
  } catch (error) {
    console.error('Error loading stored profiles:', error);
    return {};
  }
}

// Load profile from storage
export function loadProfileFromStorage(profileName: string): ProfileData | null {
  const profiles = getStoredProfiles();
  return profiles[profileName] || null;
}

// Delete profile from storage
export function deleteProfileFromStorage(profileName: string): boolean {
  try {
    const profiles = getStoredProfiles();
    delete profiles[profileName];
    localStorage.setItem('apex_profiles', JSON.stringify(profiles));
    return true;
  } catch (error) {
    console.error('Error deleting profile:', error);
    return false;
  }
}

// Export profile as JSON file
export function exportProfileAsJson(profile: ProfileData, filename: string): void {
  const dataStr = JSON.stringify(profile, null, 2);
  const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
  
  const exportFileDefaultName = `${filename}.json`;
  
  const linkElement = document.createElement('a');
  linkElement.setAttribute('href', dataUri);
  linkElement.setAttribute('download', exportFileDefaultName);
  linkElement.click();
}

// Import profile from JSON file
export function importProfileFromJson(file: File): Promise<ProfileData> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const content = e.target?.result as string;
        const profile = JSON.parse(content) as ProfileData;
        resolve(profile);
      } catch (error) {
        reject(new Error('Invalid JSON file'));
      }
    };
    reader.onerror = () => reject(new Error('Failed to read file'));
    reader.readAsText(file);
  });
}

// Convert profile to form data for editing
export function profileToFormData(profile: ProfileData): Partial<FormData> {
  return {
    purpose: profile.basic_info.purpose,
    attire: profile.basic_info.attire,
    background: profile.basic_info.background,
    vibe: profile.basic_info.vibe,
    lighting: profile.advanced_settings.lighting,
    mood: profile.advanced_settings.mood,
    age_range: profile.advanced_settings.age_range,
    gender: profile.advanced_settings.gender,
    ethnicity: profile.advanced_settings.ethnicity,
    resolution: profile.advanced_settings.resolution,
    custom_notes: profile.additional_info.custom_notes || '',
    preset_name: profile.additional_info.preset_used || undefined,
  };
}

// Utility to format file size
export function formatFileSize(bytes: number): string {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// Utility to truncate text
export function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength - 3) + '...';
}
