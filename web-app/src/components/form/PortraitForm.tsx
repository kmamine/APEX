import { useState, useCallback } from 'react';
import axios from 'axios';
import { FormSection } from './FormSection';
import { Button } from '../ui/Button';
import { Input } from '../ui/Input';
import { Select } from '../ui/Select';
import { Textarea } from '../ui/Textarea';
import { Card } from '../ui/Card';
import { FormData, ProfileData } from '../../types';
import {
  purposeOptions,
  attireOptions,
  backgroundOptions,
  vibeOptions,
  lightingOptions,
  moodOptions,
  ageRangeOptions,
  genderOptions,
  ethnicityOptions,
  resolutionOptions,
  presets,
  defaultFormValues,
} from '../../constants/options';
import {
  validateBasicInfo,
  createProfileData,
  generateAdvancedPrompt,
  saveProfileToStorage,
} from '../../utils/profileManager';
import { formatJSON } from '../../utils';

export const PortraitForm = () => {
  const [formData, setFormData] = useState<FormData>(defaultFormValues);
  const [output, setOutput] = useState('');
  const [status, setStatus] = useState('');
  const [advancedPrompt, setAdvancedPrompt] = useState('');
  const [savedFile, setSavedFile] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [jobId, setJobId] = useState<string | null>(null);
  const [imageUrl, setImageUrl] = useState<string | null>(null);

  const updateField = useCallback((field: keyof FormData, value: any) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  }, []);

  const applyPreset = useCallback((presetName: string) => {
    const preset = presets[presetName];
    if (preset) {
      setFormData(prev => ({
        ...prev,
        purpose: preset.purpose,
        attire: preset.attire,
        background: preset.background,
        vibe: preset.vibe,
        custom_notes: preset.custom_notes,
        preset_name: presetName,
      }));
      setStatus(`✨ Applied preset: ${presetName}`);
    }
  }, []);

  const clearForm = useCallback(() => {
    setFormData(defaultFormValues);
    setOutput('');
    setStatus('');
    setAdvancedPrompt('');
    setSavedFile('');
  }, []);

  const handleSubmit = useCallback(async (e: any) => {
    e.preventDefault();
    setIsLoading(true);
    setJobId(null);
    setImageUrl(null);
    try {
      // Validate basic info
      const validation = validateBasicInfo(
        formData.purpose,
        formData.attire,
        formData.background,
        formData.vibe
      );

      if (!validation.isValid) {
        setStatus(validation.message);
        return;
      }

      // Create profile data
      const profile = createProfileData(formData);
      
      // Generate advanced prompt
      const prompt = generateAdvancedPrompt(formData);
      profile.generated_prompt = prompt;

      // Save to storage if requested
      let saveMessage = '';
      if (formData.save_profile) {
        try {
          const filename = saveProfileToStorage(profile);
          saveMessage = ` | 💾 Saved to: ${filename}`;
          setSavedFile(filename);
        } catch (error) {
          saveMessage = ` | ⚠️ Save failed: ${error}`;
        }
      }

      // Update outputs
      setOutput(formatJSON(profile));
      setAdvancedPrompt(prompt);
      setStatus(`✅ Advanced style profile generated successfully!${saveMessage}`);

      // --- API call to Job Manager service ---
      try {
        const response = await axios.post('http://localhost:8000/jobs', {
          prompt: prompt,
          style: formData.resolution || 'portrait',
          seed: formData.seed || null
        });
        if (response.data && response.data.job_id) {
          setJobId(response.data.job_id);
          setStatus(prev => prev + ` | 🖼️ Job submitted: ${response.data.job_id}`);
          // imageUrl will be set after job is processed by backend
        } else {
          setStatus(prev => prev + ' | ⚠️ No job returned');
        }
      } catch (apiError) {
        setStatus(prev => prev + ` | ❌ Backend error: ${apiError}`);
      }
      // --- End API call ---
    } catch (error) {
      setStatus(`❌ Error generating profile: ${error}`);
    } finally {
      setIsLoading(false);
    }
  }, [formData]);

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            🖼️ APEX: Agentic Portrait EXperience
          </h1>
          <p className="text-xl text-gray-600 mb-2">
            Advanced Professional Portrait Preferences Form
          </p>
          <p className="text-gray-500">
            Create detailed style profiles for AI-generated professional portraits with advanced customization options.
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Left Column - Form */}
            <div className="space-y-6">
              {/* Preset Selection */}
              <Card title="🎯 Quick Start Presets" description="Choose a preset to get started quickly">
                <div className="grid-responsive gap-4">
                  <Select
                    options={Object.keys(presets).map(name => ({ value: name, label: name }))}
                    placeholder="Choose a preset..."
                    onChange={(e) => applyPreset(e.target.value)}
                  />
                  <Button
                    type="button"
                    variant="secondary"
                    onClick={() => applyPreset(formData.preset_name || '')}
                    disabled={!formData.preset_name}
                  >
                    ✨ Apply Preset
                  </Button>
                </div>
              </Card>

              {/* Basic Settings */}
              <FormSection title="🔧 Basic Settings">
                <div className="grid-responsive">
                  <Select
                    label="📌 What is the portrait for?"
                    options={purposeOptions}
                    value={formData.purpose}
                    onChange={(e) => updateField('purpose', e.target.value)}
                    placeholder="Select purpose..."
                  />
                  <Select
                    label="👔 Preferred attire"
                    options={attireOptions}
                    value={formData.attire}
                    onChange={(e) => updateField('attire', e.target.value)}
                    placeholder="Select attire..."
                  />
                  <Select
                    label="🏢 Background style"
                    options={backgroundOptions}
                    value={formData.background}
                    onChange={(e) => updateField('background', e.target.value)}
                    placeholder="Select background..."
                  />
                  <Select
                    label="😊 Desired vibe"
                    options={vibeOptions}
                    value={formData.vibe}
                    onChange={(e) => updateField('vibe', e.target.value)}
                    placeholder="Select vibe..."
                  />
                </div>
              </FormSection>

              {/* Advanced Settings */}
              <FormSection title="⚙️ Advanced Settings">
                <div className="grid-responsive">
                  <Select
                    label="💡 Lighting Style"
                    options={lightingOptions}
                    value={formData.lighting}
                    onChange={(e) => updateField('lighting', e.target.value)}
                  />
                  <Select
                    label="🎭 Overall Mood"
                    options={moodOptions}
                    value={formData.mood}
                    onChange={(e) => updateField('mood', e.target.value)}
                  />
                  <Select
                    label="🎂 Age Range"
                    options={ageRangeOptions}
                    value={formData.age_range}
                    onChange={(e) => updateField('age_range', e.target.value)}
                  />
                  <Select
                    label="👤 Gender"
                    options={genderOptions}
                    value={formData.gender}
                    onChange={(e) => updateField('gender', e.target.value)}
                  />
                  <Select
                    label="🌍 Ethnicity"
                    options={ethnicityOptions}
                    value={formData.ethnicity}
                    onChange={(e) => updateField('ethnicity', e.target.value)}
                  />
                  <Select
                    label="📐 Resolution"
                    options={resolutionOptions}
                    value={formData.resolution}
                    onChange={(e) => updateField('resolution', e.target.value)}
                  />
                </div>
              </FormSection>

              {/* Additional Info */}
              <FormSection title="📸 Additional Information">
                <div className="space-y-4">
                  <Input
                    type="file"
                    label="📸 Optional reference photo"
                    accept="image/*"
                    onChange={(e) => updateField('reference_photo', e.target.files?.[0] || null)}
                  />
                  <Textarea
                    label="📝 Additional notes & specific requirements"
                    placeholder="Describe any specific details: facial hair, glasses, jewelry, specific poses, lighting preferences, etc."
                    rows={5}
                    value={formData.custom_notes}
                    onChange={(e) => updateField('custom_notes', e.target.value)}
                  />
                </div>
              </FormSection>

              {/* Controls */}
              <Card>
                <div className="flex flex-col sm:flex-row gap-4">
                  <div className="flex items-center space-x-2">
                    <input
                      type="checkbox"
                      id="save_profile"
                      checked={formData.save_profile}
                      onChange={(e) => updateField('save_profile', e.target.checked)}
                      className="w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded focus:ring-primary-500"
                    />
                    <label htmlFor="save_profile" className="text-sm font-medium text-gray-700">
                      💾 Save profile to browser storage
                    </label>
                  </div>
                  <div className="flex gap-2 ml-auto">
                    <Button
                      type="button"
                      variant="outline"
                      onClick={clearForm}
                      disabled={isLoading}
                    >
                      🔄 Clear
                    </Button>
                    <Button
                      type="submit"
                      disabled={isLoading}
                      className="min-w-[180px]"
                    >
                      {isLoading ? '⏳ Generating...' : '🚀 Generate Profile'}
                    </Button>
                  </div>
                </div>
              </Card>
            </div>

            {/* Right Column - Output */}
            <div className="space-y-6">
              <Card title="📋 Generated Outputs">
                {status && (
                  <div className={`p-4 rounded-lg mb-4 ${
                    status.includes('✅') ? 'bg-green-50 text-green-800' : 
                    status.includes('❌') || status.includes('⚠️') ? 'bg-red-50 text-red-800' :
                    'bg-blue-50 text-blue-800'
                  }`}>
                    {status}
                  </div>
                )}

                <div className="space-y-4">
                  <Textarea
                    label="📄 Complete Style Profile (JSON)"
                    value={output}
                    readOnly
                    rows={15}
                    className="font-mono text-xs"
                  />
                  
                  <Textarea
                    label="🎨 Generated Flux Prompt"
                    value={advancedPrompt}
                    readOnly
                    rows={6}
                    className="font-mono text-sm"
                  />

                  {savedFile && (
                    <Input
                      label="💾 Saved File"
                      value={savedFile}
                      readOnly
                    />
                  )}
                  {jobId && (
                    <Input
                      label="🖼️ Image Job ID"
                      value={jobId}
                      readOnly
                    />
                  )}
                  {imageUrl && (
                    <Input
                      label="🖼️ Image URL"
                      value={imageUrl}
                      readOnly
                    />
                  )}
                </div>
              </Card>

              {/* Tips */}
              <Card title="💡 Pro Tips">
                <div className="space-y-3 text-sm text-gray-600">
                  <p><strong>📸 Reference Photos:</strong> Upload a clear headshot for better style matching</p>
                  <p><strong>💡 Lighting:</strong> "Natural Light" for warmth, "Studio Lighting" for crispness</p>
                  <p><strong>🎭 Mood:</strong> Match the mood to your industry and personal brand</p>
                  <p><strong>📐 Resolution:</strong> Use "Portrait" for vertical layouts, "Wide" for headers</p>
                  <p><strong>📝 Custom Notes:</strong> Be specific about glasses, facial hair, jewelry, etc.</p>
                </div>
              </Card>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};
